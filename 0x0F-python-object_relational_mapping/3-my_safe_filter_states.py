#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s", (state_name,))
    values= cursor.fetchall()
    for value in values:
        print(value)
    cursor.close()
    db.close()
