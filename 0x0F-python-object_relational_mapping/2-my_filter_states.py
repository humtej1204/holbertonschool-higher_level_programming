#!/usr/bin/python3
from sys import argv
import MySQLdb


def SQLconnect():
    """
    Conect to database
    """
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], password=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("Can't connect to database")
        return 0
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{name}' ORDER BY id ASC;"
                .format(name=argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db_connection.close()


SQLconnect()
