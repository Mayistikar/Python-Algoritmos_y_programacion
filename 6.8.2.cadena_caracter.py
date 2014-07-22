#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod resuelve el punto 6.8.2 de libro Algoritmos y programacion, capitulo 6, pagina 81
"""

def entre_cadena(cadena, caracter):
	"""
	Dada una cadena  y un caracter esta funcion ubica el caracter en medio de cada caracter de la cadena
	PARAMETROS:
		una cadena string
		un caracter string
	RETORNO:
		una cadena string
	"""
	lista=''
	for posicion in range(len(cadena)):
		lista+=cadena[posicion]
		lista+=","
	return lista

def espacios(cadena):
	"""
	Dada una cadena esta funcion inserta _ por cada espacio
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	lista=""
	for pos in range(len(cadena)):
		if cadena[pos]==" ":
			lista+="_"
		else:
			lista+=cadena[pos]
	return lista

def remplazar_caracteres(cadena, caracter):
	"""
	Dada una cadena esta funcion inserta X por cada Caracter
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	lista=""
	for pos in range(len(cadena)):
		lista+=caracter
	return "Su clave es "+lista

def cada_tres(cadena):
	"""
	Dada una cadena esta funcion inserta . cada tres digitos
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	lista=""
	contador=0
	for pos in range(len(cadena)):
		contador+=1
		if contador>3:
			lista+="."
			contador=1
			lista+=cadena[pos]			
		else:
			lista+=cadena[pos]			
	return lista

cadena=raw_input("Ingrese una palabra: ")
caracter=raw_input("Ingrese el caracter: ")
#print (entre_cadena(cadena, caracter))
#print espacios(cadena)
#print (remplazar_caracteres(cadena, caracter))
print cada_tres(cadena)