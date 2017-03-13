#!/usr/bin/python
import psycopg2
import sys

hostname = 'bgramire-MOBL'
username = 'postgres'
password = 'admin'
database = 'postgres'

try:
    myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    #doQuery( myConnection )
    myConnection.close()
    conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='%i'" \
              % (hostname, database, username, password, 5432)
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Falle en CBD Database connection failed!\n ->%s" % (exceptionValue))

# print the connection string we will use to connect
print
"Connecting to database\n ->%s" % (conn_string)





