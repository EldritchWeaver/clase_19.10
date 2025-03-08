from conexion import conectar_bd
import MySQLdb

def crear_registro(conexion, nombre, apellido):
    cursor = conexion.cursor()
    sql = "INSERT INTO pacientes (nombre, apellido) VALUES (%s, %s)"
    valores = (nombre, apellido)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f'Tus datos se han guardado con exito')
    cursor.close()

def leer_registro(conexion, tabla):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    resultados  = cursor.fetchall()
    # for pacientes in resultados:
    #    print(pacientes)
    cursor.close()
    return resultados

def actualizar_registro(conexion, paciente_id, nombre, apellido):
    cursor = conexion.cursor()
    try:
        sql = "UPDATE pacientes SET nombre = %s, apellido = %s WHERE ID_pacientes = %s"
        valores = (nombre, apellido, paciente_id)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Tus datos se actualizaron con exito.")
    except MySQLdb.Error as error:
        print(f'Error al actualizar el registro: {error}')
    finally:
        cursor.close()

def eliminar_registro(conexion, paciente_id):
    cursor = conexion.cursor()
    sql = "DELETE FROM pacientes WHERE ID_pacientes = %s"
    valores = (paciente_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tus datos se han eliminado con exito")
    cursor.close()
    
# if conexion:
#     leer_registros(conexion)
#     actualizar_registro(conexion, 2, 'acea', 'vaca')
#     leer_registro(conexion)
#     eliminar_registro(conexion, 1)
#     leer_registro(conexion)
#     conexion.close()


conexion = conectar_bd()

if conexion:
    leer_registro(conexion, 'pacientes')
    # leer_registro(conexion, 'clinicas')
    leer_registro(conexion, 'enfermeros')
    
    actualizar_registro(conexion, 1, 'Maria', 'Hernandez')

    conexion.close()
