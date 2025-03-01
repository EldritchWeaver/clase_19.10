# pip intsall mysql-connector-python

# Scikit-learn:
# Proporciona herramientas para el aprendizaje automatico.
# Incluye algoritmos para clasificacion, regresion, clustering y reduccion de dimensionalidad

# TensorFlow y PyTorch:
# Son bibliotecas para el aprendizaje automatico
# Permiten contruir y entrenar redes neuronales

# Flask y Django:

# OS

# Creando coneccion con lka base de datos:

import mysql.connector

def conectar_bd():
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="data"
        )
        if conexion:
            print(f'La base de datos se ha conectado con éxito: {conexion}')
            return conexion

    except mysql.connector.Error as error:
        print(f'Error al conectar a MySQL: {error}')
        return None

    except Exception as error:
        print(f'Error inesperado: {error}')
        return None

    finally:
        # Aquí podrías cerrar la conexión si es necesario
        if conexion and conexion.is_connected():
            conexion.close()
            print('Conexión cerrada.')

conexion = conectar_bd()
if conexion:
    print('Conexión exitosa.')
else:
    print('No se pudo conectar a la base de datos.')