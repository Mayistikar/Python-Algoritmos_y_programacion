#!/usr/bin/env python
#-*-coding:utf-8;-*-
"""Este soft accede a datos por parte del usuario y retorna un formula calculada"""

def formula(): #calcula el resultado de la formula en el ejercicio recibiendo datos de usuario
	pesos=input("Cual es la cantidad de pesos: ")
	interes=input("Cual es la tasa de interes: ")
	anos=input("A cuantos anos: ")
	return "el monto final es ", pesos*((1+(interes/100))**anos)

print formula()