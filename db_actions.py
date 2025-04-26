import sqlite3

conn = sqlite3.connect('sec_db_j.db', check_same_thread=False)
conn.row_factory = sqlite3.Row

def get_t_list():
    query = "SELECT DISTINCT SECID, SHORTNAME FROM stocks ORDER BY SECID ASC;"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    result = [{"ticker": row["SECID"], "name": row["SHORTNAME"]} for row in rows]
    return result


def get_data_by_ticker(ticker: str, limit_rows: int):
    cursor = conn.cursor()
    query = "SELECT SHORTNAME, SECID, PREVLEGALCLOSEPRICE, PREVDATE FROM stocks WHERE SECID = ? ORDER BY PREVDATE DESC " \
            "LIMIT ?;"
    cursor.execute(query, (ticker,limit_rows))
    rows = cursor.fetchall()
    result = [{"ticker": row["SECID"], "name": row["SHORTNAME"], "price": row["PREVLEGALCLOSEPRICE"],
               "time": row["PREVDATE"]} for row in rows]
    return result
