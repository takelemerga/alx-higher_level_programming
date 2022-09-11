#!/usr/bin/python3

"""
    script that takes in the name of a state as an argument
    and lists all cities of that state, using the
    database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    # create connection between python and database and
    # returns connection object
    con = MySQLdb.connect(host='localhost', user=argv[1],
                          passwd=argv[2], db=argv[3],
                          port=3306
                          )
    # create cursor object to execute sql  query
    cursor = con.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON state_id=states.id\
             WHERE states.name LIKE BINARY %s ORDER BY cities.id"

    cursor.execute(query, (argv[4],))
    result = cursor.fetchall()
    print(", ".join([row[0] for row in result]))
