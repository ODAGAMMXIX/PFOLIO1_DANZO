import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect("C:\\academic-test\\191016-G-danzodb.db")
    print(conn)
except Error as e:
    print(e)

def select_all_Danzo(conn):
    """    Query all rows in the tasks table     :param conn: the Connection object     :return:    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Danzo")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        print(conn)
