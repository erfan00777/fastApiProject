import clickhouse_connect
from app.config import (
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_USER,
    CLICKHOUSE_PASSWORD,
    CLICKHOUSE_DATABASE
)

# Connection pool variables
pool_size = 5
connection_pool = []


def create_client():
    global connection_pool

    if len(connection_pool) < pool_size:
        client = clickhouse_connect.get_client(
            host=CLICKHOUSE_HOST,
            port=CLICKHOUSE_PORT,
            username=CLICKHOUSE_USER,
            password=CLICKHOUSE_PASSWORD,
            database=CLICKHOUSE_DATABASE
        )
        connection_pool.append(client)


    return connection_pool.pop(0)


def release_client(client):

    global connection_pool
    connection_pool.append(client)


def create_table():
    client = create_client()

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS user_view (
    request_id String,
    user_id Int32,
    created_at DateTime,
    page_url String
) ENGINE = ReplacingMergeTree()
PARTITION BY toYYYYMM(created_at)
ORDER BY (request_id)  
SETTINGS index_granularity = 8192, deduplicate_merge_projection_mode = 'drop';
    """

    client.command(create_table_query)
    release_client(client)

## TTL created_at + INTERVAL 24 HOUR;  -- TTL set to 24 hours


def alter_table():
    client = create_client()

    create_table_query = f"""
    ALTER TABLE user_view 
    ADD PROJECTION user_page_view_projection 
    (   
    SELECT 
        user_id, 
        page_url, 
        COUNT(*) AS page_view_count 
    GROUP BY 
        user_id, 
        page_url
    );

    """

    client.command(create_table_query)
    release_client(client)


# def read_query(query: str):
#
#     client = create_client()
#     result = client.query(query)
#     release_client(client)
#     return result

def read_query(query: str):
    client = create_client()
    try:
        result = client.query(query)
        rows = result.result_rows
    finally:
        release_client(client)
    return rows

def write_query(query: str):

    client = create_client()
    client.command(query)
    release_client(client)


def close_clients():
    global connection_pool
    for client in connection_pool:
        client.close()
    connection_pool = []



