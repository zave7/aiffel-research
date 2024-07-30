import wandb
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from argparse import ArgumentParser
import psycopg2

# import wandb
# run = wandb.init(project="bookbinge_recommender", job_type="evaluate")


# # Download the model artifact
# artifact = run.use_artifact('clf_model:latest')
# model_path = artifact.download()

parser = ArgumentParser()
parser.add_argument("--model-name", dest="model_name", type=str, default="sk_model")
parser.add_argument("--version", dest="version", type=int, default=0)
args = parser.parse_args()

run = wandb.init()
artifact = run.use_artifact(f"if-zave/pipeline-test/{args.model_name}:v{args.version}", type="model")
artifact_dir = artifact.download()
print(artifact_dir)

model_pipeline_load = joblib.load(artifact_dir + "/model_pipeline_wandb.joblib")

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
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=2022)

# 3. validate
load_train_pred = model_pipeline_load.predict(X_train)
load_valid_pred = model_pipeline_load.predict(X_valid)

load_train_acc = accuracy_score(y_true=y_train, y_pred=load_train_pred)
load_valid_acc = accuracy_score(y_true=y_valid, y_pred=load_valid_pred)

print("Load Model Train Accuracy :", load_train_acc)
print("Load Model Valid Accuracy :", load_valid_acc)
