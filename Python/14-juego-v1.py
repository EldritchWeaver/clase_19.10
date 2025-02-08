# Como saber si un numero es par o impar

numero = input('Agrega un numero y te dire si es par o impar: ')

numero = int(numero)

if numero % 2 == 0:
    print(f'Tu numero: {numero}, es par')
else:
    print(f'Tu numero: {numero}, es inpar')
