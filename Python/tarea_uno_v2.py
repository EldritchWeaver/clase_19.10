#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:15:35 2025

@author: gale

Tarea 1:
    Realizar un directorio telefonico, donde el usuario pueda:
        1) Consultar por categoria o nombre del negocio.
        2) Agregar un negocio.
"""
# ___________-----Inicio de la Seccion de Funciones-----_____________ #


def mostrar_entradas():
    print('')
    print('______----ENTRADAS-----______')
    print('')
    for clave in directorio.keys():
        print(f'{clave}:')
        for entrada in directorio[clave]:
            print(f'    {entrada}')


def mostrar_categorias():
    print('')
    print('______----CATEGORIAS-----______')
    print('')
    i = 0
    for categoria in categorias:

        print(f'{i} :: {categoria}.')

        i = i + 1
    print('')


def seleccionar_categoria():
    mostrar_categorias()

    print('')
    opcion_categoria = input('Seleccione una categoria: ')
    try:
        opcion_categoria = int(opcion_categoria)
        return categorias[opcion_categoria]
    except ValueError:
        print('')
        print('Error: Dato no valido')


def consulta_por_categoria():
    categoria = seleccionar_categoria()

    print(f'____----Entradas con la categoria: {categoria}.----____')

    for clave in directorio.keys():
        for entrada in directorio[clave]:
            if categoria is not entrada:  # En este caso, is not es igual a !=
                pass
            else:
                print(f'{clave}:')
                for entrada in directorio[clave]:
                    print(f'    {entrada}')


def consulta_por_nombre():
    for clave in directorio.keys():
        print(f'- {clave}.')

    nombre_negocio = input('Ingrese el nombre de un negocio: ')
    # print(nombre_negocio)

    if nombre_negocio not in directorio.keys():
        print('Nombre no registrado. Bye!')
    else:
        # print(directorio[nombre_negocio])
        print('')
        print(f'{nombre_negocio}:')
        for entrada in directorio[nombre_negocio]:
            print(f'    {entrada}')


def agregar_un_negocio():
    print('')
    negocio = input('Ingrese el nombre del negocio: ')

    if negocio not in directorio.keys():
        telefono = input('Ingrese el telefono del negocio: ')

        categoria = seleccionar_categoria()

        directorio[negocio] = [telefono, categoria]
        mostrar_entradas()
    else:
        print('El negocio ya esta registrado.')
        opcion = input('Desea modificar los datos? s/n')

        if opcion == 's':
            print(f'{negocio}:')
            for entrada in directorio[negocio]:
                print(f'    {entrada}')

            print('')
            telefono = input('Ingrese el nuevo telefono del negocio: ')

            categoria = seleccionar_categoria()

            direccion = input('Ingrese la nueva direccion del negocio: ')

            directorio[negocio] = [telefono, categoria, direccion]

            print(f'{negocio}:')
            for entrada in directorio[negocio]:
                print(f'    {entrada}')

        elif opcion == 'n':
            print('Bye Bye!')
        else:
            print('Bye!')


# ___________-----Fin de la Seccion de Funciones-----_____________ #

# ___________-----Seccion de datos-----_____________ #


directorio = {
    'EnDigital': [
        '555-555-5555',
        'Cursos de tecnologia',
        'Sede de SanJuan, frente a la U.E.C.P Pedro Zaraza'
        ],
    'Amazon': [
        '555-555-5555',
        'Tienda Online',
        'Sin lugar fisico'
        ],
    'Platzi': [
        '555-555-5555',
        'Cursos de tecnologia',
        'Sin lugar fisico, creo'
        ],
    'Makro': [
        '555-555-5555',
        'Tienda Fisica',
        'Se donde esta, pero no se la direccion... que misterio'
        ]
    }

categorias = ['Tienda Online', 'Cursos de tecnologia', 'Tienda Fisica']

# ___________-----Fin de la seccion de datos-----_____________ #

print('Bienvenido a tu Direcctorio de Negocios!.')
print('')
print('Desea consultar por la categoria o nombre del negocio?')
print('O desea añadir uno nuevo?')
print('')
print('1 para consultar por categoria.')
print('2 para consultar por nombre.')
print('3 para añadir un negocio')

opt = input('Escoja la opcion que desee: ')

try:
    opt = int(opt)
    # consulta_por_categoria()
    # consulta_por_nombre()
    # agregar_un_negocio()

    if opt == 1 and opt in range(2):
        print('')
        consulta_por_categoria()
        print('')

    elif opt == 2 and opt in range(2):
        print('')
        consulta_por_nombre()
        print('')

    elif opt == 3 and opt in range(2):
        print('')
        agregar_un_negocio()
        print('')
    else:
        print('Bye!')

except ValueError:
    print('Error: Dato invalido. Bye!')
