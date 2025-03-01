import pyodbc

# Configura los parámetros de conexión
server = 'localhost'
database = 'data'
username = 'root'
password = ''

def conectar_bd():
    conexion = None
    try:
        # Establece la conexión usando el controlador ODBC para MySQL
        conexion = pyodbc.connect(r'DRIVER={{MySQL coneex}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        print(f'La base de datos se ha conectado con éxito: {conexion}')
        return conexion

    except pyodbc.Error as error:
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

# Conectar a la base de datos
conexion = conectar_bd()

if conexion:  # Verifica si la conexión fue exitosa
    cursor = conexion.cursor()

    # Ejecuta una consulta
    cursor.execute('SELECT * FROM pacientes')
    for row in cursor.fetchall():
        print(row)

    # Cierra la conexión
    cursor.close()  # Cierra el cursor
    conexion.close()  # Cierra la conexión