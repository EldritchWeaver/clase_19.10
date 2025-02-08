#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:13:53 2025

@author: gale

Tarea 2:

    Simular un banco donde el usuario debe poder:
        1) Consultar saldo en la cuenta.
        2) Agregar saldo.
        3) Retirar.
"""

# ___________-----Inicio de la Seccion de Funciones-----_____________ #


def verificar(dato):

    for clave in datos_cuenta.keys():
        if datos_cuenta[clave] != dato:
            login = False
        else:
            login = True
            break
    return login


def retirar():
    a_retirar = input('Ingrese saldo a retirar: ')

    try:
        a_retirar = float(a_retirar)
        if datos_cuenta['ammount'] >= a_retirar:
            datos_cuenta['ammount'] = datos_cuenta['ammount'] - a_retirar
        else:
            print('Error: Saldo Insuficiente')
    except ValueError:
        print('Error: Dato invalido. Bye')


def depositar():
    a_depositar = input('Ingrese saldo a depositar: ')

    try:
        a_depositar = float(a_depositar)
        datos_cuenta['ammount'] = datos_cuenta['ammount'] + a_depositar
    except ValueError:
        print('Error: Dato invalido. Bye')

# ___________-----Fin de la Seccion de Funciones-----_____________ #

# ___________-----Seccion de datos-----_____________ #


datos_cuenta = {'user': 'en',
                'password': '12',
                'ammount': 0.0}

acceso = [False, False]  # En ejecucion. debe cambiar a [True, True]

# ___________-----Fin de la seccion de datos-----_____________ #


usuario = input('Ingrese su nombre de usuario: ')
acceso[0] = verificar(usuario)

contrasena = input('ingrese su contraseña: ')
acceso[1] = verificar(contrasena)

# print(login)

if acceso[0] is not True and acceso[1] is not True:

    print('Error: El usuario o la contraseña son incorrectos. Bye!')

else:
    claves = ['user', 'password', 'ammount']

    print(f'Bienvenido, {datos_cuenta[claves[0]]}!.')
    print(f'Su saldo es de: {datos_cuenta[claves[2]]}')

    print('')
    print('Desea depositar, retirar dinero o consultar saldo?')
    opcion = input('1 para depositar, 2 para retirar o 3 para consultar: ')

    try:
        opcion = int(opcion)

        if opcion == 1:
            print('')
            depositar()
            print('')
            print(f'Ahora su saldo es de: {datos_cuenta[claves[2]]}. Bye!')

        elif opcion == 2:
            print('')
            retirar()
            print('')
            print(f'Ahora su saldo es de: {datos_cuenta[claves[2]]}. Bye!')

        elif opcion == 3:
            print('')
            print(f'Su saldo es de: {datos_cuenta[claves[2]]}. Bye!')
        else:
            print('Respuesta incorrecta. Bye!')

    except ValueError:
        print('Error: Dato invalido. Bye!')
