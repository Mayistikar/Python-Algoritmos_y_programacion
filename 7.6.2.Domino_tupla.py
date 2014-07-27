#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este codigo determina si dos fichas de domino representadas por dos tuplas respectivamente ((3,4) y (1,1)) encajan;
Resuelve el punto 7.6.2 del libro Algoritmos y programacion del capitulo 7 pagina 98
"""

def encajan(tupla1, tupla2):
	"""
	Evalua cada posicion de tupla 1 y si esta corresponde con alguna posicion
	de tupla 2 determina correspondencia
	"""
	for pos in tupla1:		
		if pos==tupla2[0] or pos==tupla2[1]:
			return "Las fichas encajan"
	return "Las fichas no encajan"

def separar(cadena1, cadena2):
	"""
	Separa las cadenas en tuplas cada una y si las envia para ser evauladas en 
	la funcion encajan.
	"""
	cad1=cadena1.split('-')
	cad2=cadena2.split("-")
	return encajan(cad1, cad2)

tupla1=(2,1)
tupla2=(3,4)
cadena1=raw_input("Ingrese la ficha 1: ")
cadena2=raw_input("Ingrese la ficha 2: ")

print encajan(tupla1,tupla2)
print 
print separar(cadena1, cadena2)


