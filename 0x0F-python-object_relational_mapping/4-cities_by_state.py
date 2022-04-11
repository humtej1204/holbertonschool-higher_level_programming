#!/usr/bin/python3
from sys import argv
import MySQLdb


def sqlConection():
    """
    Conecting and quering to database
    """
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306,
                                        user=argv[1], password=argv[2],
                                        db=argv[3], charset="utf8")
    except Exception:
        print("Can't connect to database")
        return 0
    cur = db_connection.cursor()
    sql = "SELECT c.id,c.name, s.name FROM cities AS c JOIN states AS s "
    strin = "WHERE c.state_id=s.id ORDER BY id ASC"
    sqlc = sql + strin
    cur.execute(sqlc)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_connection.close()


sqlConection()
