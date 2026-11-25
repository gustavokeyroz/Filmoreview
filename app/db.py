import os
import pymysql
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote

load_dotenv()

def get_db():

    database_url = os.getenv("DATABASE_URL")

    if database_url:
        url = urlparse(database_url)

        return pymysql.connect(
            host=url.hostname,
            port=url.port or 3306,
            user=unquote(url.username),
            password=unquote(url.password),
            database=url.path.lstrip("/"),
            cursorclass=pymysql.cursors.DictCursor,
            charset="utf8mb4"
        )

    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor,
        charset="utf8mb4"
    )
