#!/usr/bin/python3
"""this  scripts lists all cities in the databse"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
        FROM cities\
        JOIN states\
        ON cities.state_id=states.id")
    """Obtaining Query Results"""
    rows = cur.fetchall()
    for iten in rows:
        print(iten)
