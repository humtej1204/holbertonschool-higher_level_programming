#!/usr/bin/python3
import MySQLdb
from sys import argv


def sqlConection():
    """
    Conecting a quering to database
    """
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], password=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("Can't connect to database")
        return 0
    cur = db_connection.cursor()
    sql = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    data = (argv[4],)
    cur.execute(sql, data)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db_connection.close()


sqlConection()
