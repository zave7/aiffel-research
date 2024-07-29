import pandas as pd
from sklearn.datasets import load_iris, fetch_california_housing
import psycopg2

def get_data(dataset):
    
    if dataset == "iris":
        X, y = load_iris(return_X_y=True, as_frame=True)
        df = pd.concat([X, y], axis="columns")
        rename_rule = {
            "sepal length (cm)": "sepal_length",
            "sepal width (cm)": "sepal_width",
            "petal length (cm)": "petal_length",
            "petal width (cm)": "petal_width",
        }
        df = df.rename(columns=rename_rule)
    elif dataset == "california_housing":
        X, y = fetch_california_housing(return_X_y=True, as_frame=True)
        df = pd.concat([X, y], axis="columns")
    return df

def insert_data(db_connect, dataset, data):
    if dataset == "iris":
        insert_row_query = f"""
        INSERT INTO iris_data
        (timestamp, sepal_length, sepal_width, petal_length, petal_width, target)
        VALUES (
            NOW(),
            {data.sepal_length},
            {data.sepal_width},
            {data.petal_length},
            {data.petal_width},
            {data.target}
        );"""
    elif dataset == "california_housing":
        insert_row_query = f"""
        INSERT INTO california_housing
        (timestamp, med_inc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude, med_house_val)
        VALUES (
            NOW(),
            {data.MedInc},
            {data.HouseAge},
            {data.AveRooms},
            {data.AveBedrms},
            {data.Population},
            {data.AveOccup},
            {data.Latitude},
            {data.Longitude},
            {data.MedHouseVal}
        );"""
    print(insert_row_query)
    with db_connect.cursor() as cur:
        cur.execute(insert_row_query)
        db_connect.commit()
        
if __name__ == "__main__":
    db_connect = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="localhost",
        port=5432
    )
    
    data = get_data()
    insert_data(db_connect, data.sample(1).squeeze())