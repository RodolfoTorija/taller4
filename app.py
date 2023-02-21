from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    port ="3306",
    user= "root",
    password = "Zeromainj0.",
    database = "clinica_azul"
)

@app.route('/verificar', methods = ['POST'])
def verificar():
    nombre = request.form['nombreusuario']
    contrasena = request.form['contrasena']

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM usuarios WHERE nombre = %s AND contrasena = %s", (nombre, contrasena))

    usuario = mycursor.fetchone()

    if usuario:
        return "Inicio de sesión exitoso"
    else:
        return "Nombre de usuario o contraseña incorrectos"

    


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


if __name__ == '__main__':
    app.run()

