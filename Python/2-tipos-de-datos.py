# Tipos de Datos

nombre = 'Lucia'                                    #String o cadena de texto
edad = 30                                           #Entero
altura = 1.71                                       #Flotante. No es un entero!
es_estudiante = True                                #Booleano
lista_de_compras = ['manzanas', 'banana', 'leche']  #Lista -> arrays
tupla_de_coordenadas = (10, 20, 11.12)              #Tupla
persona = {'nombre': nombre, 'edad': edad}          #Diccionario -> objetos

print(nombre, edad, altura, es_estudiante)
print(lista_de_compras)
print(tupla_de_coordenadas)
print(persona)

print(lista_de_compras[1])


phone = {
    'modelo': "redmi 12C",
    'pantalla': "1014x780",
    'bateria': "5000 Mw",
    'procesador': "snap dragon",
    'memoria': "8 GB",
    'almacenamiento': "256 GB",
    'camara': "nose MgPx",
    'carcasa': "hola",
    'sistema poperativo': "Android"
}

print(phone.get('modelo'))
