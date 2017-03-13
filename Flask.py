#!flask/bin/python
import time
from WebBot.Conexion import *
from flask import Flask
from flask import Flask, request, jsonify, json, Response
from WebBot.Execute import *
import uuid
import hashlib
import datetime

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


@app.route('/api/cds/titulo/hash', methods=['GET'])
def metodoHash():
    # mystring = input('Enter String to hash: ')
    # Assumes the default UTF-8
    mystring = "Gaby-Web-Bot"
    hash_object = hashlib.md5(mystring.encode())
    hash = hash_object.hexdigest()
    creadora = "Gabriela Ramirez"
    fecha = "Viernes que viene"
    saveInfo(mystring, hash, creadora, fecha)
    return "Nombre: " + mystring + "\n" + "Hash: " + hash_object.hexdigest() + "\n" + "Creadora: " + "Gabriela Ramirez" + "\n" + "Fecha: " + "Viernes que viene";


@app.route('/api/ejemplo2')
def ejemplo_2():
    return "Ejemplo 2"


@app.route('/api/estados')
def estados():
    sal = mostrarEstados()
    retorno = ""
    retorno = str(sal)
    if(retorno == "[]"):
        retorno = "Ahorita el WebBot no sabe hacer nada"
    return retorno


@app.route('/api/ejemplo_param')
def ejemplo_param():
    ip = request.environ['REMOTE_ADDR']
    in_args = request.args  # Primero Obtener los Parametros
    param = float(in_args['dato_enviado'])  # Seleccionar el parametro deseado
    param1 = float(in_args['dato_enviado1'])
    param2 = in_args['dato_enviado2']
    condicion = ""
    if param2 == "-":

        result = param - param1
        condicion= "El Web Bot sabe Restar"

    elif param2 == "*":

        result = param * param1
        condicion = "El Web Bot sabe Multiplicar"

    elif param2 == "/":

        result = param / param1
        condicion = "El Web Bot sabe Dividir"

    else:
        param2 = "+"
        result = param + param1
        condicion = "El Web Bot sabe Sumar"

    res = str(result)

    condicion +=" El resultado es " + res

    saveLogs(ip, time.strftime("%d/%m/%y"), time.strftime("%H:%M:%S"), param, param1, param2, result)

    resp = Response(json.dumps(condicion), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp


@app.route('/api/desaprender_param')
def desaprender_param():
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
    resp = Response(json.dumps(result), status=200, mimetype='application/json')  # Configurar el tipo de respuesta
    resp.headers['Link'] = "www.mi-web-bot.com"
    return resp

## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')






