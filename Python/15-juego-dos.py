# Ejercicio N2

pregunta = input('Agrega un numero y te dire si es inpar: ')
pregunta += '/n Escribe "cerrar" para salir de la app: '
preguntar = True

while True:
    numero = input('Ingresa un número (o escribe "cerrar" para salir): ')

    if numero.lower() == 'cerrar':
        break

    try:
        numero = int(numero)

        if numero % 2 == 0:
            print(f'Tu numero: {numero}, es par')
        else:
            print(f'Tu numero: {numero}, es inpar')

    except ValueError:
        print('Error: Dato nvalido')
