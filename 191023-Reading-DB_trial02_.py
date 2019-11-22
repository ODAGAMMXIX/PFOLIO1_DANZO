import sqlite3
from sqlite3 import Error
#conn = None
#    try:
conn = sqlite3.connect(r'C:\academic-test\191016-G-danzodb.db')
#return conn
#    except Error as e:
#print(r'C:\academic-test\191016-G-danzodb.db')
#return conn
def select_all_tasks(conn):
    """    Query all rows in the tasks table     :param conn: the Connection object     :return:    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        print(conn)
