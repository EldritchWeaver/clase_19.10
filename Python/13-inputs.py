nombre = input('Cuál es tu nombre? \n')
print(f'Tu nombre es: {nombre}')

#Leer los datos cuando sean numeros podemos hacer un if
#Nota: las entradas de datos siempre vienen en string

edad = input('Cual es tu edad? \n')
#Convertir edad en un entero
""" edad = int(edad) #Float #str

if edad >= 18:
    print(f'Eres mayor de edad y puedes votar')
else:
    print(f'Lo sentimos, aun eres un bebé') """

#caso de que un usuario ingrese otro valor que no sea un numero
try:
    edad = int(edad)
    if edad >= 18:
        print(f'Eres mayor de edad y puedes votar.')
    else:
        print(f'Aun no tienes la edad para votar.')
except ValueError:
    print('Por favor, ingrese un numero valido para la edad')