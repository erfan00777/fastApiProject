from dotenv import load_dotenv
import os

load_dotenv()

CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST", "host")
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT", "port")
CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER", "user")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD", "password")
CLICKHOUSE_DATABASE = os.getenv("CLICKHOUSE_DATABASE", "database")


