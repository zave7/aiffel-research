from time import sleep
from connection import get_connection
from data_insertion import get_data, insert_data
from argparse import ArgumentParser
from table_creator import create_table
    
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--db-host", dest="db_host", type=str, default="localhost")
    args = parser.parse_args()
    data = get_data()
    connect = get_connection(host=args.db_host)

    create_table(connect)
    
    for idx, row in data.iterrows():
        insert_data(connect, row)
        sleep(0.5)