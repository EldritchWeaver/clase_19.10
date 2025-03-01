import mysql.connector
import mysql

# Establecer la conexión
conexion = mysql.connector.connect(
    host="localhost",        # Cambia esto si tu base de datos está en otro servidor
    user="root",       # Reemplaza con tu nombre de usuario
    password="", # Reemplaza con tu contraseña
    database="data" # Reemplaza con el nombre de tu base de datos
)

# my_cursor = conexion.cursor()

def crear_registro(conexion, nombre, apellido):
    cursor = conexion.cursor()
    sql = "INSERT INTO pacientes (nombre, apellido) VALUES (%s, %s)"
    valores = (nombre, apellido)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f'Tus datos se han guardado con exito')
    cursor.close()

def leer_registro(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pacientes")
    resultados  = cursor.fetchall()
    for pacientes in resultados:
        print(pacientes)
    cursor.close

def leer_registro_medico(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pacientes")
    resultados  = cursor.fetchall()
    for pacientes in resultados:
        print(pacientes)
    cursor.close

def actualizar_registro(conexion, paciente_id, nombre, apellido):
    cursor = conexion.cursor()
    try:
        sql = "UPDATE pacientes SET nombre = %s, apellido = %s WHERE paciente_id = %s"
        valores = (nombre, apellido, paciente_id)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Tus datos se actualizaron con exito.")
    except mysql.connector.Error as error:
        print(f'Error al actualizar el registro: {error}')
    finally:
        cursor.close()

def eliminar_registro(conexion, paciente_id):
    cursor = conexion.cursor()
    sql = "DELETE FROM pacientes WHERE paciente_id = %s"
    valores = (paciente_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tus datos se han eliminado con exito")
    cursor.close()
    
if conexion:
    # leer_registros(conexion)
    actualizar_registro(conexion, 2, 'acea', 'vaca')
    leer_registro(conexion)
    # eliminar_registro(conexion, 4)
    conexion.close()
