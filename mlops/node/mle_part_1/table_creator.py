import psycopg2
import pandas as pd
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True, as_frame=True)
df = pd.concat([X, y], axis="columns")

print(df)
print(df.dtypes)

# cur = db_connect.cursor()
# cur.execute(create_table_query)
# db_connect.commit()
# cur.close()

def create_table(db_connect, dataset):
    if dataset == "iris":
        create_table_query = """
        CREATE TABLE IF NOT EXISTS iris_data(
            id SERIAL PRIMARY KEY,
            timestamp timestamp,
            sepal_length float8,
            sepal_width float8,
            petal_length float8,
            petal_width float8,
            target int
        );
        """
    elif dataset == "california_housing":
        create_table_query = """
        CREATE TABLE IF NOT EXISTS california_housing(
            id SERIAL PRIMARY KEY,
            timestamp timestamp,
            med_inc float8,
            house_age float8,
            ave_rooms float8,
            ave_bedrms float8,
            population float8,
            ave_occup float8,
            latitude float8,
            longitude float8,
            medHouseVal float8
        );
        """
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()

if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host="localhost",
        port=5432,
        database="mydatabase"
    )
    create_table(db_connect)