import os

def crear_archivo(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('Este es el contenido inicial del archivo. \n')
        print(f'Archivo: {nombre_archivo} ha sido creado exitosamente.')

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()  # Lee todo el contenido
            print(contenido)  # Imprime el contenido del archivo creado en la parte de 
    except FileNotFoundError:
        print(f'El archivo: {nombre_archivo} no existe.')  # Error si el archivo no existe

def agregar_linea(nombre_archivo, nueva_linea):
     with open(nombre_archivo, 'a') as archivo:
        archivo.write(nueva_linea + '\n')
        print('La linea ha sido agregada exitosamente.')

def eliminar_archivo(nombre_archivo):
    try:
        os.remove(nombre_archivo)
        print(f'Archivo: {nombre_archivo} eliminado')
    except FileNotFoundError:
        print(f'El archivo: {nombre_archivo}, no existe')

# Ejemplo de uso:
nombre_archivo = 'mi_archivo.txt'
crear_archivo(nombre_archivo)
leer_archivo(nombre_archivo)
agregar_linea(nombre_archivo, 'Viva la vida.')
leer_archivo(nombre_archivo)
# eliminar_archivo(nombre_archivo)