import sqlite3
import pandas as pd

conn = sqlite3.connect('moex_db.db')
conn.row_factory = sqlite3.Row
#query = "SELECT * FROM stocks;"
#df = pd.read_sql(query, conn)

def get_t_list():
    query = "SELECT DISTINCT name, ticker FROM stocks;"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    result = [{"ticker": row["ticker"], "name": row["name"]} for row in rows]
    return result
