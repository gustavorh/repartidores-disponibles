# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:34:22 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

import math

# La siguiente función recibe como parámetros los diccionarios de repartidores, usuarios y visitas y un código de usuario


def buscar_repartidor(diccionario_repartidores, diccionario_usuarios, diccionario_visitas, codigo_usuario):
    # Retornar una lista de repartidores disponibles y cercanos, de manera ascendente
    # según el número de visitas que estos hayan realizado al usuario requerido.
    #
    # Un repartidor se encontrará cercano si está ubicado a menos de 4km del usuario.
    # Si no hay repartidores cercanos, devolver una lista vacía.

    # For loop que recorre la los valores del diccionario de usuarios y obtiene la ubicación de cada usuario.
    diccionario_ubicaciones = {}
    for usuario in diccionario_usuarios.values():
        x_usuario, y_usuario = usuario

    # For loop que recorre la los valores del diccionario de repartidores y obtiene la ubicación de cada repartidor.
    for repartidor in diccionario_repartidores.values():
        ubicacion, disponibilidad = repartidor
        #print(f"Ubicacion: {ubicacion}, Disponibilidad: {disponibilidad}")
        x_repartidor = ubicacion[0]
        y_repartidor = ubicacion[1]

        #print(f" X U: {x_usuario} , Y U: {y_usuario} ; X R: {x_repartidor} , Y R: {y_repartidor}\n")

    """
    for valores in diccionario_visitas.values(): # For loop que recorre los valores del diccionario, en este caso la lista de tuplas con el usuario y cantidad de visitas.
        for tuplas in valores: # For loop que recorre las tuplas de la lista
            usuario, n_visitas = tuplas
            print(usuario, n_visitas)
    """

    pass
    # return repartidores_disponibles


# Llave: nombre ; Valor: tupla con (ubicación del repartidor) y su estado de (disponiblidad)
repartidores = {
    "Jose Gaete": ((10, 2), True),
    "Gina Gomez": ((9, 3), True),
    "Hugo Cepeda": ((5, 5), False)
}

# Llave: usuario ; Valor: (ubicación del usuario)
usuarios = {
    1431: (5, 2),
    825: (8, 2),
    273: (10, 1)
}

# Llave: nombre repartidor ; Valor: [(codigo usuario, n° visitas), (codigo usuario, n° visitas), (codigo usuario, n° visitas)]
visitas = {
    "Jose Gaete": [(1431, 5), (825, 8), (273, 2)],
    "Gina Gomez": [(1431, 2), (825, 5), (273, 3)],
    "Hugo Cepeda": [(1431, 8), (825, 2), (273, 1)]
}

# Programa principal preguntando por el código de un usuario
cod_usuario = int(input("Ingrese un código de usuario: "))

# Llamado a la función para obtener la lista de repartidores disponibles y cercanos según el código de usuario y visitas al mismo
repartidores_disponibles = buscar_repartidor(
    repartidores, usuarios, visitas, 1431)  # cod_usuario
print(repartidores_disponibles)
