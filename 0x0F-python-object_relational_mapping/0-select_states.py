#!/usr/bin/python

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        database = MySQLdb.connect(
                host='localhost',
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                port=3306
                )

    except Exception:
        print("No se puede acceder a la base de datos.")
        exit()

    def show_data():
        cursor = database.cursor()
        cursor.execute('SELECT * FROM states')
        table = cursor.fetchall()
        if table:
            for row in table:
                print(row)
        cursor.close()

    show_data()
    database.close()
