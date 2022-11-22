"""Execute a query without params and return all results as a list"""

from database_operations.operations import execute_connection


def execute_query(sql):
    """Execute a query without params and return all results as a list"""
    conn = execute_connection()
    with conn.cursor() as cur:
        cur.execute(sql)
        response = cur.fetchall()
    return response
