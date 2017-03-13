#!flask/bin/python
import time
from Conexion import *
from flask import Flask
from flask import Flask, request, jsonify, json, Response
from Execute import *
import uuid
import hashlib
import datetime
import requests

# This is an example of the Flask uses Json to solve some problems ;)
# by marguedas


app = Flask(__name__)

json_var = {
    "widget":
        {
            "debug": "on",
            "window": {
                "title": "Sample Konfabulator Widget",
                "name": "main_window",
                "width": 500,
                "height": 500
            },
            "image": {
                "src": "Images/Sun.png",
                "name": "sun1",
                "hOffset": 250,
                "vOffset": 250,
                "alignment": "center"
            },
            "text": {
                "data": "Click Here",
                "size": 36,
                "style": "bold",
                "name": "text1",
                "hOffset": 250,
                "vOffset": 100,
                "alignment": "center",
                "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
            }

        }
}

def create_hash(value):
    val = value + datetime.datetime.now().isoformat()
    return hashlib.sha1(val).hexdigest()

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/')
def index():
    json_result = json_var
    js = json.dumps(json_result)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://ecommerce.com'

    return resp

@app.route('/api/ejemplo1', methods=['GET'])
def ejemplo_1():
    return "Ejemplo 2"

@app.route('/api/cds/titulo/autor/<nombre>', methods=['GET'])
def ejemplo_cds(nombre):
    return "Gaby-Web-Bot" + "\n" + " Algo"

@app.route('/api/cds/titulo/hash', methods=['GET']) #Genera la informacion
def metodoHash():
    # mystring = input('Enter String to hash: ')
    # Assumes the default UTF-8
    mystring = "Gaby-Web-Bot"
    hash_object = hashlib.md5(mystring.encode()) #Metodo que genera la llave hash usando MD5
    hash = hash_object.hexdigest()
    creadora = "Gabriela Ramirez"
    fecha = "10-Marzo-17"
    saveInfo(mystring, hash, creadora, fecha)
    return "Nombre: " + mystring + "\n" + "Hash: " + hash_object.hexdigest() + "\n" + "Creadora: " + "Gabriela Ramirez" + "\n" + "Fecha: " + "10-Marzo-17";


@app.route('/api')
def api():
    in_args = request.args  # Primero Obtener los Parametros
    #url = "https://samples.openweathermap.org/data/2.5/forecast/daily?id=524901&appid=b1b15e88fa797225412429c1c50c122a1"
    url = "https://randomuser.me/api/"
    data = requests.get(url).json()

    json_result = data
    js = json.dumps(json_result)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://ecommerce.com'

    return resp


@app.route('/api/estados')
def estados():
    sal = mostrarEstados() #Me Devuelve lo que el Webbot sabe
    retorno = ""
    #retorno = str(sal)
    if(sal == ""):
        retorno = "Ahorita el WebBot no sabe hacer nada"
    else:
        retorno = sal
    return retorno

@app.route('/api/sumar')
def sumar():
    ip = request.environ['REMOTE_ADDR']
    in_args = request.args  # Primero Obtener los Parametros
    suma = 0
    respuesta = consulta("+") #Consulto si sabe o no sabe

    if respuesta == "si":
        for row in in_args:
            try:
                suma += int(in_args[row])
            except:
                print("El parametro es null")
        condicion = "El resultado de la suma es " + str(suma)
    else:
        condicion = "El WebBot aun no sabe sumar"

    resp = Response(json.dumps(condicion), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp

@app.route('/api/restar')
def restar():
    ip = request.environ['REMOTE_ADDR']
    in_args = request.args  # Primero Obtener los Parametros
    resta = 0
    cont= 0
    respuesta = consulta("-") #Consulto si sabe o no sabe

    if respuesta == "si":
        for row in in_args:
            try:
                if(cont == 0):
                   resta = int(in_args[row])
                else:
                    resta -= int(in_args[row])
                cont += 1
            except:
                print("El parametro es null")
        condicion = "El resultado de la resta es " + str(resta)
    else:
        condicion = "El WebBot aun no sabe restar"

    resp = Response(json.dumps(condicion), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp

@app.route('/api/dividir')
def dividir():
    ip = request.environ['REMOTE_ADDR']
    in_args = request.args  # Primero Obtener los Parametros
    division = 1
    respuesta = consulta("/") #Consulto si sabe o no sabe

    if respuesta == "si":
        for row in in_args:
            try:
                aux= int(in_args[row])
                division = aux/division
            except:
                print("El parametro es null")
        condicion = "El resultado de la division es " + str(division)
    else:
        condicion = "El WebBot aun no sabe dividir"

    resp = Response(json.dumps(condicion), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp

@app.route('/api/multiplicar')
def multiplicar():
    ip = request.environ['REMOTE_ADDR']
    in_args = request.args  # Primero Obtener los Parametros
    multiplicacion =1
    respuesta = consulta("*") #Consulto si sabe o no sabe

    if respuesta == "si":
        for row in in_args:
            try:
                multiplicacion *= int(in_args[row])
            except:
                print("El parametro es null")
        condicion = "El resultado de la multiplicacion es " + str(multiplicacion)
    else:
        condicion = "El WebBot aun no sabe multiplicar"

    resp = Response(json.dumps(condicion), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp

@app.route('/api/aprender')
def aprender():
    ip = request.environ['REMOTE_ADDR']
    in_args = request.args  # Primero Obtener los Parametros
    param = in_args['dato_enviado']  # Seleccionar el parametro deseado
    condicion = ""
    if param == "restar":
        condicion= "El Web Bot sabe Restar"

    elif param == "multiplicar":
        condicion = "El Web Bot sabe Multiplicar"

    elif param == "dividir":
        condicion = "El Web Bot sabe Dividir"

    elif param == "sumar":
        condicion = "El Web Bot sabe Sumar"
    else:
        condicion = "Escriba un valor valido"

    aprender_BD(param)  #Mando los datos para que aprenda
    saveLogs(ip+ " ", time.strftime("%d/%m/%y "), time.strftime("%H:%M:%S "), "enseno_a_"+ param+ " ","Gaby ") #Guarda la informacion de los reggistros
    resp = Response(json.dumps(condicion), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp

@app.route('/api/desaprender_param')
def desaprender_param():
    ip = request.environ['REMOTE_ADDR']
    in_args = request.args  # Primero Obtener los Parametros
    param =in_args['dato_enviado']  # Seleccionar el parametro deseado

    if param == "-":
      result = "El web ya no sabe restar"

    elif param == "*":
      result = "El web ya no sabe multiplicar"

    elif param == "/":
      result = "El web ya no sabe dividir"

    else:
        param = "+"
        result = "El web ya no sabe sumar"

    deleteEstado(param)
    saveLogs(ip+ " ", time.strftime("%d/%m/%y "), time.strftime("%H:%M:%S "), "olvido_" + param + " ",
             "Gaby ")  # Guarda la informacion de los reggistros
    resp = Response(json.dumps(result), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp

@app.route('/api/webbot/actividad_reciente', methods=['GET'])
def actividad_reciente():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        ip= ""
        fecha = ""
        hora  = ""
        numero1 = ""
        usuario = ""
        cursor.execute("SELECT * FROM logs")
        for row in cursor:
            ip+= str(row[0])
        cursor.execute("SELECT * FROM logs")
        for row in cursor:
            fecha += str(row[1])
        cursor.execute("SELECT * FROM logs")
        for row in cursor:
            hora += str(row[2])
        cursor.execute("SELECT * FROM logs")
        for row in cursor:
                numero1+= str(row[3])
        cursor.execute("SELECT * FROM logs")
        for row in cursor:
            usuario += str(row[4])

        result = {
            "Log de operaciones":
                {
                    "Realizada por": ip.split(" "),

                    "Fecha": fecha.split(" "),

                    "Hora": hora.split(" "),

                    "Accion realizada": numero1.split(" "),

                    "Usuario": usuario.split(" "),

                }
        }


    except:
            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            sys.exit("Save Logs Database connection failed!\n ->%s" % (exceptionValue))

    resp = Response(json.dumps(result), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp

## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')

