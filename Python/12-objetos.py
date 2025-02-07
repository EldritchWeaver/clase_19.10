# OBJETOs
# Un objeto como nyasabem,os es similar a un array,
# te permite agrupar contenido
# Diferentes, tipos de datos
# En python son llamados diccionarios

cancion = {
    'artista': 'Ricardo Arjona',
    'nombre': 'El Problema'
}

# acceder a los elementos de los diccionarios
print(cancion['artista'])

artista = cancion['artista']
print(artista)

# Agregar una key al diccionario
cancion['playlist_id'] = 'Romantica'
print(cancion)

# Eliminar una key al diccionario
del cancion['playlist_id']
print(cancion)

# ___________-----EJERCICIO-----_____________ #

ordenador = {
    'CPU': 'AMD Ryzen 9 7900x',
    'disco_duro': 'Kingstom 500GB SSD M.2 NVMe',
    'GPU': 'NVIDIA GeForce RTX4800',
    'RAM': '16GB'
}
pc = ordenador['CPU']
print(pc)
print(ordenador)
