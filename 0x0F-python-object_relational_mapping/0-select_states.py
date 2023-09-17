#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
     rows = c.fetchall()
    for i in rows:
        print(i)
    db.close()
    c.close()
