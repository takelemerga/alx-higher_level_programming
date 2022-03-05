#!/usr/bin/python3

import MySQLdb
from sys import argv
"""
    script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':

    # create connection between python and database and
    # returns connection object
    con = MySQLdb.connect(host='localhost', user=argv[1],
                          passwd=argv[2], db=argv[3],
                          port=3306
                          )
    # create cursor object to execute sql  query
    cursor = con.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON state_id = states.id ORDER BY cities.id"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
