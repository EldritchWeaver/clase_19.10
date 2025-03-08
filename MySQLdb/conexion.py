# pip install mysql-client

import MySQLdb

def save_data(data):
    archivo = open('data.txt', 'w')
        
    for dato in data:
        print(dato)
        archivo.write(f'{dato} \n')

    archivo.close()
    

def conectar_bd():
    conexion = None
    try:
        conexion = MySQLdb.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="data"
        )
        if conexion:
            print(f'La base de datos se ha conectado con éxito: {conexion}')
            return conexion

    except MySQLdb.Error as error:
        print(f'Error al conectar a MySQL: {error}')
        return None

    except Exception as error:
        print(f'Error inesperado: {error}')
        return None

conexion = conectar_bd()

if conexion:
    try:
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM pacientes")
        resultados_uno = cursor.fetchall()
        # cursor.execute("SELECT * FROM enfermeros")
        # resultados_dos = cursor.fetchall()
        # cursor.execute("SELECT * FROM clinicas")
        # resultados_tres = cursor.fetchall()

        # save_data(resultados_uno)
        # save_data(resultados_dos)
        # save_data(resultados_tres)

    except MySQLdb.Error as e:
        print(f'Error en la consulta: {e}')
    
    finally:
        cursor.close()
        conexion.close()
        print("Conexion cerrada...")
