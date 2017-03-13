from Flask import *
import psycopg2
import sys
from WebBot.Conexion import *

def mostrarEstados():
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        cursor.execute("SELECT definicion FROM Estados")
        salida = []
        rows = cursor.fetchall()
        for row in rows:
            salida.append(row)
        return salida

    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Falle en Save Logs Database connection failed!\n ->%s" % (exceptionValue))


def deleteEstado(sim):
    try:
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Estados WHERE simbolo = %s", (sim))

        conn.commit()
    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Falle en Save Logs Database connection failed!\n ->%s" % (exceptionValue))

def saveLogs(ip, date,time, number1, number2, sign,solution):
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        cursor.execute("insert into Logs (ip,fecha,hora,numero1,numero2,sign,solucion) values (%s,%s,%s,%s,%s,%s,%s)", [ip, date,time, number1, number2, sign,solution])
        definicion = ""
        if sign == "+":
            definicion = "suma"
        elif sign == "-":
            definicion = "resta"
        elif sign == "*":
            definicion = "multiplicacion"
        elif sign == "/":
            definicion = "division"
        cursor.execute("insert into Estados (simbolo,definicion) values (%s,%s)",[sign,definicion])
        conn.commit()
    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Falle en Save Logs Database connection failed!\n ->%s" % (exceptionValue))

def saveInfo(nombre, hash, creadora, fecha):
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        cursor.execute(
        "insert into info (nombre,hash,creadora,fecha) values (%s,%s,%s,%s)",
        [nombre, hash, creadora, fecha])

        conn.commit()
    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Falle en Save Logs Database connection failed!\n ->%s" % (exceptionValue))


# post para que aprenda...
