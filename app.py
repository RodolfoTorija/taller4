from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from flask_mysqldb import MySQL
from jinja2 import Template

app = Flask(__name__)






@app.route("/")
def index():
    return render_template("index.html")

@app.route('/index.html')
def index_inicio():
    return render_template("index.html")

@app.route('/especialidades.html')
def especialidades():
    return render_template("especialidades.html")

@app.route('/servicios.html')
def servicios():
    return render_template("servicios.html")


@app.route('/quienessomos.html')
def quienessomos():
    return render_template("quienessomos.html")

@app.route('/contactanos.html')
def contactanos():
    return render_template("contactanos.html")

# Configuración de la base de datos
...


try:
    mydb = mysql.connector.connect(
        host = "localhost",
        port = "3306",
        user= "root",
        password = "Zeromainj0.",
        database = "clinica_azul"
    )

    print("Conexión exitosa a la base de datos. \n")

except mysql.connector.Error as error:
    print("Error al conectarse a la base de datos: {}".format(error))
    mydb = None

#Conexion de base de datos
@app.route('/verificar', methods = ['GET','POST'])
def verificar():
    if mydb is None:
        return render_template('/index.html', mensaje='Error al conectarse a la base de datos')

    nombre = request.form['form2Example11']
    contrasena = request.form['form2Example22']

    try:
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM usuarios WHERE nombre = %s AND contrasena = %s", (nombre, contrasena))

        usuario = mycursor.fetchone()

        if usuario:
            print("Inicio correctametne")
            # Inicio de sesión exitoso
            return render_template('/index.html')
        else:
            print("No se inicio correctamente")
            # Nombre de usuario o contraseña incorrectos
            return render_template('/index.html', error='Nombre de usuario o contraseña incorrectos')

    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta a la base de datos: {}".format(error))
        return render_template('/index.html', error='Error al ejecutar la consulta a la base de datos')




if __name__ == '__main__':
    app.run()

