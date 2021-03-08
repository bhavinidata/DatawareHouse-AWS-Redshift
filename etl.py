import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

# Load songs and user logs data (JSON files) from S3 bucket to staging tables.
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        print(f"Executed copy query: {query}" )
        conn.commit()

# Insert data from staging table to fact and dimention table.
def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        print(f"Executed insert query: {query}" )
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()