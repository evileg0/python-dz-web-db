import sqlite3
import pandas as pd

conn = sqlite3.connect('moex_db.db', check_same_thread=False)
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


def get_data_by_ticker(ticker: str):
    cursor = conn.cursor()
    query = "SELECT name, ticker, percent, price, time FROM stocks WHERE ticker = ?;"
    cursor.execute(query, (ticker,))
    rows = cursor.fetchall()
    result = [{"ticker": row["ticker"], "name": row["name"], "percent": row["percent"], "price": row["price"],
               "time": row["time"]} for row in rows]
    return result
