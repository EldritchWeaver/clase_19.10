playlist = {}
playlist['canciones'] = []


def app():
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar tu playlist? escriba el nombre aqui: ')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False  # Ya tenemos un nombre, desactivamos el True
            agregar_canciones()
            mostrar_resumen()


def agregar_canciones():
    print(f'Agregando canciones a la playlist: {playlist['nombre']}')

    while True:
        cancion = input('Ingrese el nombre de la cancion (o "x" para salir): ')
        
        if cancion.lower() == 'x':
            break

        playlist['canciones'].append(cancion)

        print(f'Cancion agregada: {cancion}')
    print('Playlis Completa: /n')
    print(playlist)


def eliminar_canciones():
    print(f'Eliminandio canciones de la playlis: {playlist['nombre']}')

    while True:
        cancion_eliminar = input('Ingresa el nombre de la cancion a eliminar (ó "x" para salir): ')

        if cancion_eliminar.lower() == 'x':
            break

        if cancion_eliminar in playlist['canciones']:
            playlist['canciones'].remove(cancion_eliminar)
            print(f'Cancion eliminada: {cancion_eliminar}')
        else:
            print('La cancion no se encuentra en la playlist.')
        print('¡Playlist Actualizada!')


def mostrar_resumen():
    print(f'Playlist: {playlist['nombre']}')
    print('Canciones de la playlist: ')
    for cancion in playlist['canciones']:
        print(cancion)

app()
