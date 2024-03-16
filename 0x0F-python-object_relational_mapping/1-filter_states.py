#!/usr/bin/python3
""" list a value naemstart with n """
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE
            name LIKE 'N%' ORDER BY id ASC")
    values = cursor.fetchall()
    for value in values:
        print(value)
    cursor.close()
    db.close()
