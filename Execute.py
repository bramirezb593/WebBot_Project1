from Flask import *
import psycopg2
import sys
from Conexion import *

def mostrarEstados(): #dice lo que el bot sabe hacer
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string) # Obtiene la conexion a la base de datos
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor() #Creamos un cursor
        cursor.execute("SELECT definicion FROM Estados")
        sal = ""
        rows = cursor.fetchall()
        for row in rows:
            #salida.append(row)
            sal += row[0] + "\n"
        return sal

    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Falle en Save Logs Database connection failed!\n ->%s" % (exceptionValue))

def aprender_BD(parametro):
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        salida = ""
        param =  str(parametro)
        cursor.execute("SELECT simbolo FROM sign where significado = %s",[param])
        for row in cursor:
            salida += str(row[0])
        cursor.execute("insert into Estados (simbolo,definicion) values (%s,%s)", [salida, param])
        conn.commit()
    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Falle en Save Logs Database connection failed!\n ->%s" % (exceptionValue))

def consulta(parametro):
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        salida = ""
        cursor.execute("SELECT simbolo FROM estados where simbolo = %s",[parametro])
        for row in cursor:
            salida += str(row[0])
        if salida != "":
            return "si"
        else:
            return "no"


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

def saveLogs(ip, date,time, number1,usuario):
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        cursor.execute("insert into Logs (ip,fecha,hora,numero1,usuario) values (%s,%s,%s,%s,%s)", [ip, date,time, number1,usuario])
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

