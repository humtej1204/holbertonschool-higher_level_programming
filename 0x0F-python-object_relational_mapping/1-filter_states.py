#!/usr/bin/python3
from sys import argv
import MySQLdb


def connectDB():
    """
    Connect to database and quering
    """
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], password=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("Can't connect to database")
        return 0
    cur = db_connection.cursor()
    sql = "SELECT id, name FROM states ORDER BY id ASC;"
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        if 'N' == row[1][0]:
            print(row)
    cur.close()
    db_connection.close()


connectDB()
