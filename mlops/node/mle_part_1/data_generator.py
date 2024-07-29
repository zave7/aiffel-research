from time import sleep
from connection import get_connection
from data_insertion import get_data, insert_data
from argparse import ArgumentParser
from table_creator import create_table
    
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--db-host", dest="db_host", type=str, default="localhost")
    parser.add_argument("--dataset", dest="dataset", type=str, default="iris")
    args = parser.parse_args()
    connect = get_connection(host=args.db_host)
    data = get_data(args.dataset)

    create_table(connect, args.dataset)
    
    for idx, row in data.iterrows():
        insert_data(connect, args.dataset, row)
        sleep(0.5)