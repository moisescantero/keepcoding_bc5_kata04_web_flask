from flask import Flask#importar flask de la clase Flask (framework)
app = Flask(__name__)#crear aplicación vacía - instanciar flask(pasando parámetro nombre o no rula) y guardar en variable llamada app

@app.route("/")#ruta para punto de entrada(recurso) a nuestra app web, la barra(/) es nuestro index para saber que hemos llegado a servidor
def index():
    return "Hola mundo"

#para levantar este servidor de mentira necesitamos crear 2 variables de entorno de las que Flask usará:
#para crearlas en el terminal escribimos set FLASK_APP=run.py y
#set FLASK_CONFIG=development
#para acabar ejecutamos flask run y debe entregar una IP para abrir en el navegador con el texto "hola mundo"