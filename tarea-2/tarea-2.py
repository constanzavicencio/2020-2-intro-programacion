# -*- coding: utf-8 -*-
"""Tarea 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15vo-m7O7FQn53ESw8Wn7Pnd-_85L-Agn
"""

# primero, importamos las funciones auxiliares que necesitaremos
import estructura
from abstraccion import *
from lista import *
from estadisticas import *
# queremos crear un programa interactivo que haga un recuento de los votos del Plebiscito Consituyente de 2020

# Se define mediante una funcion la variable listaDeDatos a partir de los datos ingresados por el usuario
# Es una funcion recursiva, pues se debe poder seguir ingresando datos hasta que el usuario ingrese "fin"
def listaDatos():
  circunscripcion=input("Circunscripcion (o 'fin' para terminar) ")
  if circunscripcion=="fin":
    return None
  else:
    numeroMesa=int(input("Número de la mesa "))
    apruebo=int(input("Número de votos opción 'Apruebo' "))
    rechazo=int(input("Número de votos opción 'Rechazo' "))
    resultado=resultadoMesa(circunscripcion,numeroMesa,apruebo,rechazo)
    listaDeDatos=lista(resultado,listaDatos())
    return listaDeDatos

# estadisticasBasicas: lista -> str
# Nos entrega el total de votos por el "apruebo" y por el "rechazo" (por separado) del conjunto completo de datos ingresados
def estadisticasBasicas(listaDeDatos):
  print("Estadísticas Básicas:")
  print("Totales Plebiscito Constituyente")
  print("Total Opción Apruebo: ", totalVotosFinales(listaDeDatos,"apruebo"))
  print("Total Opción Rechazo: ", totalVotosFinales(listaDeDatos,"rechazo"))

# estadisticasAvanzadas: lista -> str
# Nos entrega la mesa con mayor cantidad de votos, indicando su circunscripcion, numero de mesa y suma total de votos
def estadisticasAvanzadas(listaDeDatos):
  if listaDeDatos==None:
    print("Estadísticas Avanzadas:")
    print("Mesa con más concurrencia: No hay datos ingresados")
  else:
    print("Estadísticas Avanzadas:")
    mesaMasConcurrida=mesaConMasVotos(listaDeDatos)
    datos=buscaMesa(listaDeDatos,mesaMasConcurrida.circunscripcion,mesaMasConcurrida.numeroMesa)
    print("Mesa con mas concurrencia: ",mesaMasConcurrida.circunscripcion,", mesa",mesaMasConcurrida.numeroMesa,", con",sumaVotosMesa(mesaMasConcurrida),"votantes")

# circunscripcionInteres: lista -> str
# Esta funcion nos entrega los datos de la cantidad de votos por "apruebo" y por "rechazo" (por separado) de la circunscripcion que sea del interes del usuario
def circunscripcionInteres(listaDeDatos):
  circunscripcion=input("Circunscripción de su interés: ")
  if circunscripcion==None:
    return "Circunscripción no válida"
  else:
    print("Votación en circunscripción ", circunscripcion, ":")
    print("Apruebo: ", totalesPorCircunscripcion(listaDeDatos,circunscripcion,"apruebo"), " Rechazo: ", totalesPorCircunscripcion(listaDeDatos,circunscripcion,"rechazo"))

# PROGRAMA PRINCIPAL
print("Bienvenido al sistema de estadísticas Plebiscito Constituyente 2020")
print("Ingrese los resultados por mesa")
def sistemaEstadisticas():
  datosIngresados=listaDatos()
  estadisticasBasicas(datosIngresados)
  estadisticasAvanzadas(datosIngresados)
  circunscripcionInteres(datosIngresados)

# Se llama a la funcion para ejecutar el programa
sistemaEstadisticas()