def app():
    archivo = open('archivo.txt', 'w')  # w: write, r: read, a: append

    # Escribir en el archivo
    for i in range(0, 10):
        archivo.write(f'Esta es la linea {i} \n')
    archivo.close()  # Cerrar el archivo

app()

# 'r': Solo lectura (modo por defecto)
# 'w': Solo escritura (sobreescribe el archivo si existe)
# 'a': Añade (añade al final del archivo)
# 'x': Crear (crea un nuevo archivo, si ya existe lanza un error)
# 'b': Binario (para abrir un achivo binario)
# '+': Leer y escribir