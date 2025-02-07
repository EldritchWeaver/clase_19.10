# Condicional if, elif, else
""" tipo = 'estudiante'

if tipo == 'estudiante':
    print('Tienes un descuento del 50%')
elif tipo == 'profesor':
    print('Tienes un descuento del 80%')
elif tipo == 'invitado':
    print('Tienes un descuento del 10%')
else:
    print('No hay descuento') """


# ___________-----EJERCICIO-----_____________ #
"""
def mostrar(type):
    print(f'El usuario es: {type}')
    return True

def verificar_user_type(user_type):
    if user_type == 'root':
        return mostrar(user_type)
    elif user_type == 'admin':
        return mostrar(user_type)
    elif user_type == 'guest':
        return mostrar(user_type)
    else:
        print('No hay tipo de usuario:
              usuario no esta registrado en ninguna base de datos')
        return False

user_list = [
    {
        'user_name': 'Gmoreno58',
        'user_type': 'root',
        'user_id': '001'
    },
    {
        'user_name': 'Gmoreno58',
        'user_type': 'admin',
        'user_id': '002'
    }
]
for user in user_list:
    var = verificar_user_type(user_list.get(user_type))
    if var

     """


def mostrar(user_type):
    print(f'El usuario es: {user_type}')
    return True


def verificar_user_type(user_type):
    if user_type in ['root', 'admin', 'guest']:
        return mostrar(user_type)
    else:
        print('No hay tipo de usuario: usuario no está registrado')
        return False


user_list = [
    {
        'user_name': 'Gmoreno58',
        'user_type': 'root',
        'user_id': '001'
    },
    {
        'user_name': 'Gmoreno58',
        'user_type': 'admin',
        'user_id': '002'
    }
]


for user in user_list:
    var = verificar_user_type(user['user_type'])
    if var:
        print(f"Nombre de usuario: {user['user_name']}")
        print(f"Tipo de usuario verificado: {user['user_type']}")
