#Operadores de comparacion/logicos

# ==   Igual a
# !=   Diferente de
# <    Menor que
# >    Mayor que
# <=   Menor o igual que
# >=   Mayor o igual que

a = 5
b = 3

igual = a == b # igual almacena el resultado de la comparacion, entonces es False
diferente = a != b # diferente almacena: True
mayor = a >= b # mayor almacena: True

print(igual, diferente, mayor)


#Condicionales

ahorro = -1
if ahorro >= 0:
    print('Nos vamos de viaje')
else:
    print('No tenemos ahorro')

#Revisamos si un valor es diferente en python string
lenguaje = 'python'
if not lenguaje == 'python':
    print(f'Super, eres un crack en {lenguaje}')
else:
    print(f'Sorry, no eres un crack de {lenguaje}')


#Evaluacion Boleana
usuatrio_autenticado = False
if usuatrio_autenticado:
    print('El usuario se atentico con exito')
else:
    print('El usuario no se autentico, vuelva a intentarlo')


#Condicionales con Listas
super_heroes = ['SuperMan', 'SpiderMan', 'WonderWoman', 'IronMan']
if 'SuperMan' in super_heroes:
    print('Amas a BatMan')
else:
    print('Tu super heroe no e BatMan')

#practica
vuedojuegos = ['Minecraft', 'BloodStrike', 'League of Legends', 'God of War', 'Stardew Valley']
juego = 'Minecraft'
if juego in vuedojuegos:
    print(f'Soy un crack en {juego}')
else:
    print(f'Soy un noob en {juego}')