import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_db():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        cursorclass=pymysql.cursors.DictCursor
    )