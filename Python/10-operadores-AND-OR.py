#Condicionales AND y OR
#AND revisa que ambas condicionales sean verdaderas
#OR revisa al menos una de las condicionales se cumpla

acceso_usuario = True
acceso_admin = False

if acceso_usuario and acceso_admin:
    print(f'Full Acces')
elif acceso_usuario:
    print(f'El usuario esta autenticado')
else:
    print(f'El usuario no esta autenticado')