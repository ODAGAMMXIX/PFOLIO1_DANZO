#READING FROM DB.
import sqlite3
from sqlite3 import Error


def create_connection(r"C:\academic-test")
def create_connection(r"C:\academic-test\191016-G-danzodb.db"):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("C:\\academic-test\\191016-G-danzodb.db")
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)

