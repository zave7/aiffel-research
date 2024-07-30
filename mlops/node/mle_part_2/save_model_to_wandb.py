import wandb
from argparse import ArgumentParser

import pandas as pd
import psycopg2
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import joblib

# 1. get data
db_connect = psycopg2.connect(
    user="myuser",
    password="mypassword",
    host="localhost",
    port=5432,
    database="mydatabase",
)
df = pd.read_sql("SELECT * FROM iris_data ORDER BY id DESC LIMIT 100", db_connect)

X = df.drop(["id", "timestamp", "target"], axis="columns")
y = df["target"]
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=42)

# 2. model development and train
model_pipeline = Pipeline([("scaler", StandardScaler()), ("svc", SVC())])
model_pipeline.fit(X_train, y_train)

train_pred = model_pipeline.predict(X_train)
valid_pred = model_pipeline.predict(X_valid)

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)

print("Train Accuracy :", train_acc)
print("Valid Accuracy :", valid_acc)

joblib.dump(model_pipeline, "model_pipeline_wandb.joblib")

# weight and bias

# Initialize a new run
run = wandb.init(project="pipeline-test", job_type="train")

metrics = {"train_acc": train_acc, "valid_acc":valid_acc}
artifact = wandb.Artifact("sk_model", type="model", description="support vector machine",
               metadata={"metrics": metrics})

artifact.add_file("model_pipeline_wandb.joblib")

run.log_artifact(artifact)

run.finish()