#Funciones y Metodos

#FUNCIONES

#Primero se define la variable y luego se llama
def saludo():
    print('Soy un aprendiz')
saludo()

def informacion(nombre = 'alguien', cargo = 'un vago'): #Se colocan valores por defecto para evitar errores si falta algun parametro al llamar la funcion
    print(f'Soy {nombre}, y soy {cargo}')
informacion('Gabriel', 'Estudiande de informatica')
informacion()

def entregar_comida(nombre = 'Jose', plato = 'boloñesa'):
    print(f'Aqui tiene su {plato}, Mr.{nombre}')
    
#nombre = input('ingrese su nombre: ')
#plato = input('Ingrese su plato favorito: ')
#entregar_comida(nombre, plato)
entregar_comida()

print(' ')

#Funciones que retornan un valor
def info(nombre):
    return nombre
empleado = info('Ramos')
print(empleado)

def sumar(a, b):
    return a + b
resultado = sumar(15, 23)
print(resultado)

def multi(a, b):
    return a * b
multiplica = multi(13, 14)
print(multiplica)


#METODOS

#Funciones: vemos la fucnione y le psasmos un valor, ej: def suma(a, b): return a+ b
#metodos: tenemos la variable, un punto, y el nombre de la funcion/metodo, ej: variable.metodo()

ciudad = 'caracas'

def mostrar_ciudad(ciudad):
    print(f'Muestrame la ciudad de {ciudad}')
mostrar_ciudad('Maracay')

print(ciudad.lower())
print(ciudad.upper())
print(ciudad.capitalize())