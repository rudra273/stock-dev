# services/postgres.py

import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine
import pandas as pd

host_name = 'db'
database_name = "mydb"
user_name = 'rudra'
password_ = '1234'
port_ = 5432


def connection(func):
    def wrapper(*args, **kwargs):
        connection = None
        try:
            connection = psycopg2.connect(
                host=host_name,
                database=database_name,
                user=user_name,
                password=password_,
                port=port_
            )
            result = func(connection, *args, **kwargs)
            return result
        except Exception as error:
            print(f'Error connecting to the database: {error}')
        finally:
            if connection:
                connection.close()
                print("Connection closed.")
    return wrapper


@connection
def dump_to_postgresql(connection, df, schema_name, table_name):
    try:
        engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)
        df.to_sql(table_name, engine, schema=schema_name, if_exists='replace', index=False)
    except Exception as e:
        print(f"Error dumping data into {schema_name}.{table_name} table: {e}")


@connection
def fetch_data_from_pg(connection, schema_name, table_or_view_name, query, params):
    try:
        engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)
        df = pd.read_sql(query, engine, params=params)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

@connection
def fetch_data_from_pg2(connection, schema_name, table_or_view_name, query):
    try:
        engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None   

