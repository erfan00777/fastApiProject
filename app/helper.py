from clickhouse_connect import Client
from app.config import (
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_USER,
    CLICKHOUSE_PASSWORD,
    CLICKHOUSE_DATABASE
)


client = None

def get_client():

    global client
    if client is None:
        client = Client(
            host=CLICKHOUSE_HOST,
            port=CLICKHOUSE_PORT,
            username=CLICKHOUSE_USER,
            password=CLICKHOUSE_PASSWORD,
            database=CLICKHOUSE_DATABASE,
            pool_min_size=5,
            pool_max_size=20
        )
    return client

def execute_query(query: str, params: tuple = ()):

    return get_client().execute(query, params)

def close_client():

    global client
    if client:
        client.close()
        client = None