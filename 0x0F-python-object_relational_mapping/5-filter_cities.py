#!/usr/bin/python3
""" lists all states from the database """
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
            passwd=mysql_password,
            user=mysql_user,
            db=database_name
            )
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM
                   cities INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s""", (state_name,))
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))
    cursor.close()
    db.close()
