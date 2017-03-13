#!/usr/bin/python
import psycopg2
import sys


hostname = '127.0.0.1'
username = 'postgres'
password = 'bjs070702'
database = 'WebBot'


#print "Using psycopg2…"
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


#try:
    # get a connection, if a connect cannot be made an exception will be raised here
#    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
#    cursor = conn.cursor()
#    cursor.execute("insert into Personas(nombre)values (%s)", ["Gaby"])
#    conn.commit()
#    cursor.execute("SELECT * FROM pg_user")
#    for row in cursor:
#     print   (row)

#     print
#    "Connected!\n"
#except:
    # Get the most recent exception
#    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
#    sys.exit("Falle en CBD Database connection failed!\n ->%s" % (exceptionValue))


