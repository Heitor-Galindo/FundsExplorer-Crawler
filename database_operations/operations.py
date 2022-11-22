"""Open database conn"""

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def execute_connection():
    """Connect to database"""
    conn = psycopg.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DATABASE"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASS"),
    )
    return conn
