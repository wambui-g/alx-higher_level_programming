#!/usr/bin/python3
"""
script that takes an argument and displays
values whose state matches arguement
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    access to the database
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \ 
            ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
