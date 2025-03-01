import pyodbc

# Inicializa el nombre del controlador
driver_name = ''
driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]

# Verifica si se encontró un controlador
if driver_names:
    driver_name = driver_names[0]

if driver_name:
    # Construye la cadena de conexión
    conn_str = 'DRIVER={};SERVER=myserver;DATABASE=mydatabase;UID=myuserid;PWD=mypassword'.format(driver_name)

    # Conectar a la base de datos
    try:
        conexion = pyodbc.connect(conn_str)
        print('Conexión exitosa a la base de datos.')
        
        # Realizar operaciones en la base de datos
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM EMP")
        for row in cursor.fetchall():
            print(row)

    except pyodbc.Error as error:
        print(f'Error al conectar a la base de datos: {error}')

    finally:
        if 'conexion' in locals() and conexion:
            cursor.close()
            conexion.close()
            print('Conexión cerrada.')
else:
    print('(No suitable driver found. Cannot connect.)')