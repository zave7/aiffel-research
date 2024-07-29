import psycopg2

def get_connection(host="localhost"):
    connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        database="mydatabase",
        host=host,
        port=5432
    )
    return connect