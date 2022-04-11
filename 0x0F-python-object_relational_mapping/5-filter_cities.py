#!/usr/bin/python3
from sys import argv
import MySQLdb


def sqlConection():
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], password=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("Can't connect to database")
        return 0
    cur = db_connection.cursor()
    string = "SELECT c.name FROM cities AS c JOIN states AS s ON \
            c.state_id=s.id WHERE s.name = '{name}' ORDER BY c.state_id ASC"
    cur.execute(string.format(name=argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row != query_rows[-1]:
            print(row[0], end=", ")
        else:
            print(row[0], end="")
    print()
    cur.close()
    db_connection.close()


sqlConection()
