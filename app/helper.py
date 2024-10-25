import clickhouse_connect
from app.config import (
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_USER,
    CLICKHOUSE_PASSWORD,
    CLICKHOUSE_DATABASE
)


client = None

def create_client():

    global client
    if client is None:
        client = clickhouse_connect.get_client(
                                    host=CLICKHOUSE_HOST,
                                    port=CLICKHOUSE_PORT,
                                    username=CLICKHOUSE_USER,
                                    password=CLICKHOUSE_PASSWORD,
                                    database=CLICKHOUSE_DATABASE
                                    # pool_min_size=5,
                                    # pool_max_size=20
        )
    return client


def create_table():

    client = create_client()

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS user_view (
        user_id Int32,
        created_at DateTime,
        page_url String
    ) ENGINE = ReplacingMergeTree()
    PARTITION BY toYYYYMM(created_at)
    ORDER BY (user_id, created_at)
    SETTINGS index_granularity = 8192
    """

    client.command(create_table_query)


def execute_query(query: str, params: tuple = ()):

    return create_client().execute(query, params)

def close_client():

    global client
    if client:
        client.close()
        client = None

