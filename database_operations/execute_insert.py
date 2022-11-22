"""Insert data into database"""

from psycopg import Error
from database_operations.operations import execute_connection


def execute_insert(sql, data):
    """Insert data into database"""
    conn = execute_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(sql, data)
    except Error as error:
        print(f"DATABASE LOG: \n{error}")
        return False
    else:
        conn.commit()
        return True
