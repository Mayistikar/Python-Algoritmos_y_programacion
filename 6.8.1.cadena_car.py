#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Resuelve el punto 6.8.1 del libro algoritmos y programacion, capitulo 6, pagina 81;
"""

def dos_primeros(cadena):
	"""
	Dada una cadena esta funcion imprime los dos primeros caracteres
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	return cadena[0:2]

def tres_ultimos(cadena):
	"""
	Dada una cadena esta funcion imprime los tres ultimos caracteres
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	return cadena[-3:(len(cadena))]

def saltando_uno(cadena):
	"""
	Dada una cadena esta funcion imprime saltando un caracter
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	return cadena[::2]

def doble__sentido(cadena):
	sentido_inverso=""
	for caracter in range(len(cadena)):
		sentido_inverso+=cadena[(len(cadena)-1)-caracter]
	return cadena+sentido_inverso

cadena=raw_input("Ingrese una palabra: ")
print dos_primeros(cadena)
print tres_ultimos(cadena)
print saltando_uno(cadena)
print doble__sentido(cadena)