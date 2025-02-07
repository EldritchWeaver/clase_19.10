#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:18:25 2025

@author: gale

Tarea 1:
    Realizar un directorio telefonico,
    donde el usuario pueda consultar
    por categoria o nombre del negocio
    y agregar un negocio.
"""

# ___________-----Inicio de la Seccion de Funciones-----_____________ #


def validar_num(dato, min_num, max_num):
    try:
        dato = int(dato)
        if dato in range(min_num, max_num + 1):
            return dato
    except ValueError:
        print('Por favor, ingrese un dato valido, vuelva a intentar \n')
        mostrar_menu()


def validar_tex(dato):
    if dato is str:
        dat = dato
        return dat

    print('Por favor, ingrese un dato valido, vuelva a intentar \n')
    agregar_entrada()


def mostrar_menu():
    print('______----MENU-----______')
    print('1 :: Ver directorio')
    print('2 :: Añadir entrada')
    print('3 :: Eliminar entrada')
    print('4 :: Añadir categoria')
    print('5 :: Eliminar categoria')
    print('6 :: Buscar entrada por categoria')
    print('7 :: Ver categorias')
    print('8 :: Salir')
    print('__________________________')

    opcion_menu = input('Ingrese su opcion: ')

    return validar_num(opcion_menu, 1, 8)


def agregar_entrada():
    negocio = input('Ingrese el nombre del negocio \n')

    telefono = input('Ingrese el telefono del negocio \n')

    categoria = asignar_categoria()

    directorio[negocio] = [telefono, categoria]

    if negocio not in directorio.keys():
        print('Error al aadir la entrada, regresando al menu principal')
        mostrar_menu()
    else:
        print('Entrada añadida correctamente, regresando al menu prinipal...')


def eliminar_entrada():
    mostrar_entradas()

    clave = input('Escriba el nombre de la entrada a eliminar: \n')

    if clave not in directorio.keys():
        print('Error: Entrada no registrada \n')
        mostrar_menu()
    else:
        del directorio[clave]


def asignar_categoria():
    var = mostrar_categorias()
    opcion_categoria = input('Seleccione una categoria \n')

    try:
        opt = int(opcion_categoria)
    except Exception:
        print('Error: Dato no valido')

    validar_num(opt, 0, var)

    return categorias[opt]


def registar_categoria():
    categoria = input('Coloque el nombre de la nueva categoria \n')

    categorias.append(categoria)

    if categoria in categorias:
        print(f'{categoria}. a sido añadida exitosamente.')

    else:
        print('Error: la categoria no se pudo añadir. vuelva a intentar')
        print('Regresando al menu principal...')
        mostrar_menu()


def eliminar_categoria():
    var = mostrar_categorias()
    opcion_categoria = input('Seleccione la categoria a eliminar \n')

    try:
        opt = int(opcion_categoria)
    except Exception:
        print('Error: Dato no valido')

    validar_num(opt, 0, var)

    categoria = categorias[opt]

    del categorias[opt]

    for clave in directorio.keys():
        for entrada in directorio[clave]:
            if categoria is not entrada:
                pass
            else:
                directorio[clave].remove(categoria)


def mostrar_entradas():
    print('______----ENTRADAS-----______')
    for clave in directorio.keys():
        print(f'{clave} :')
        for entrada in directorio[clave]:
            print(f'    {entrada}')


def mostrar_categorias():
    print('______----CATEGORIAS-----______')
    i = 0
    for categoria in categorias:

        print(f'{i} :: {categoria} \n')

        i = i + 1

    return i


def buscar_entrada_por_categoria():
    categoria = asignar_categoria()

    print(f'____----Entradas con la categoria: {categoria}.----____')

    for clave in directorio.keys():
        for entrada in directorio[clave]:
            if categoria is not entrada:
                pass
            else:
                print(f'{clave} :')
                print(f'    {entrada}')

# ___________-----Fin de la Seccion de Funciones-----_____________ #

# ___________-----Seccion de datos-----_____________ #


directorio = {
    'EnDigital': ['555-555-5555', 'Cursos de tecnologia'],
    'Amazon': ['555-555-5555', 'Tienda Online'],
    'Platzy': ['555-555-5555', 'Cursos de tecnologia'],
    'Ebay': ['555-555-5555', 'Tienda Online']
    }

categorias = ['Tienda Online', 'Cursos de tecnologia', 'Tienda de Moda']

# ___________-----Fin de la seccion de datos-----_____________ #


opcion = mostrar_menu()

if opcion == 1:
    mostrar_entradas()
    """
    opcion = input('Desea volver a mostrar el menu? s/n')
    if opcion not in ('s', 'n'):
        print('Error:Dato invalido... Vuelva a intentar')
        opcion = input('Desea volver a mostrar el menu? s/n')
    else:
        opcion = mostrar_menu()
    """

elif opcion == 2:
    agregar_entrada()
    mostrar_entradas()

elif opcion == 3:
    eliminar_entrada()
    mostrar_entradas()

elif opcion == 4:
    registar_categoria()
    mostrar_categorias()

elif opcion == 5:
    mostrar_categorias()
    mostrar_entradas()

    eliminar_categoria()

    mostrar_categorias()
    mostrar_entradas()

elif opcion == 6:
    buscar_entrada_por_categoria()

elif opcion == 7:
    mostrar_categorias()

elif opcion == 8:
    print('Saliendo...')
    pass

else:
    print('Error: opcion no valida')
