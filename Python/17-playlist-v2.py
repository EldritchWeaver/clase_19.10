playlist = {}


def crear_playlist():
    nombre_playlist = input('Como deseas nombrear tu playlist?, ingrese el nombre aqui: ')
    playlist[nombre_playlist] = []
    return nombre_playlist


def agregar_cancion(playlist_nombre):
    print(f'Agreagr canciones a la playlist: {playlist_nombre}')
    while True:
        cancion = input('ingresar el nombre de la cancion (o "x" para salir): ')
        if cancion.lower() == 'x':
            break
        playlist[playlist_nombre].append(cancion)
        print(f'Cancion agregada: {cancion}')


def eliminar_canciones(playlist_nombre):
    print(f'Eliminandio canciones de la playlis: {playlist_nombre}')

    while True:
        cancion_eliminar = input('Ingresa el nombre de la cancion a eliminar (ó "x" para salir): ')

        if cancion_eliminar.lower() == 'x':
            break

        if cancion_eliminar in playlist[playlist_nombre]:
            playlist[playlist_nombre].remove(cancion_eliminar)
            print(f'Cancion eliminada: {cancion_eliminar}')
        else:
            print('La cancion no se encuentra en la playlist.')
        print('¡Playlist Actualizada!')


def mostrar_playlist():
    nombre_playlist = nombre_playlist
    if not playlist:
        print('No hay playlist creadas.')
    else:
        for canciones in playlist.items():
            print(f'Playlist: {nombre_playlist}')
            for cancion in canciones:
                print(f'- {cancion}')


def app():
    while True:
        print("Menu")
        print('1 :: Crear una nueva Playlist.')
        print('2 :: Agregar canciones a una Playlist.')
        print('3 :: Eliminar canciones de una Playlist.')
        print('4 :: Mostrar todas las Playlist.')
        print('5 :: Salir')

        opcion = input('\n\r Seleccione una opcion: ')

        if opcion == '1':
            nombre_playlist = crear_playlist()
            agregar_cancion(nombre_playlist)
        elif opcion == '2':
            nombre_playlist = input('A que playlist deseas agregar canciones?: ')
            if nombre_playlist in playlist:
                agregar_cancion(nombre_playlist)
            else:
                print('La Playlist no existe.')
        elif opcion == '3':
            nombre_playlist = input('De que playlist desea eliminar canciones?: ')
            if nombre_playlist in playlist:
                eliminar_canciones(nombre_playlist)
            else:
                print('La playlist no existe.')
        elif opcion == '4':
            mostrar_playlist()
        elif opcion == '5':
            break
        else:
            print('Opcopn invalida.')

app()
