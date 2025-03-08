# pip install jinja2

from flask import Flask, render_template
from conexion import conectar_bd
from crud import leer_registro


app = Flask(__name__)

conexion = conectar_bd()
leer_registro(conexion, 'pacientes')
conexion.close()

@app.route("/")
def mostrar_pacientes():
    conexion = conectar_bd()
    resultados = leer_registro(conexion, 'pacientes')
    conexion.close()
    return render_template("index.html", pacientes=resultados)

if __name__ == "__main__":
    app.run(debug=True)
