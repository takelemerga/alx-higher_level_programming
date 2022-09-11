#!/usr/bin/python3

"""
   script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa
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
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
