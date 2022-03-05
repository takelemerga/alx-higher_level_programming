#!/usr/bin/python3

import MySQLdb
from sys import argv
"""
  displays all values in the states table of hbtn_0e_0_usa
  that is safe from MySQL injections
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
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))
    result = cursor.fetchall()
    for row in result:
        print(row)
