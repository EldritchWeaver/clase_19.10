import mysql.connector

# Configura los parámetros de conexión
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'data',
}

# Establece la conexión
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Ejecuta una consulta
cursor.execute('SELECT * FROM pacientes')
for row in cursor.fetchall():
    print(row)

# Cierra la conexión
conn.close()