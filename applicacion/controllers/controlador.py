from applicacion import app
from flask import render_template

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'BIENVENIDOS AL JUEGO!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

#Cuando un usuario visite http://localhost:5000/play, 
# haz que muestre tres cajas azules hermosas. Utiliza una plantilla para renderizar esto. 

@app.route('/play') 
def nivel_1():
    return render_template("nivel1.html")

@app.route('/play/<int:numero>') 
def nivel_2(numero):
    return render_template("nivel2.html", numero=numero)

@app.route('/play/<int:numero>/<string:color>') 
def nivel_3(numero,color):
    return render_template("nivel3.html", numero=numero, color=color)
