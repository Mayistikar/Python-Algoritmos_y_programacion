#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod resuelve el punto 6.8.2 de libro Algoritmos y programacion, capitulo 6, pagina 81
"""

def entre_cadena(cadena, caracter, cantidad):
	"""
	Dada una cadena  y un caracter esta funcion ubica el caracter en medio de cada caracter de la cadena
	modifica la cadena SOLO hasta la posicion "cantidad"
	PARAMETROS:
		una cadena string
		un caracter string
	RETORNO:
		una cadena string
	"""
	lista=''

	for posicion in range(len(cadena)):
		lista+=cadena[posicion]
		if posicion < cantidad:
			lista+=","
	return lista

def espacios(cadena, cantidad):
	"""
	Dada una cadena esta funcion inserta _ por cada espacio
	modifica la cadena SOLO hasta la posicion "cantidad"
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	lista=""
	contador=0
	for pos in range(len(cadena)):
		if cadena[pos]==" " and contador<cantidad:
			lista+="_"
			contador+=1
		else:
			lista+=cadena[pos]
	return lista

def remplazar_caracteres(cadena, caracter, cantidad):
	"""
	Dada una cadena esta funcion inserta X por cada Caracter
	modifica la cadena SOLO hasta la posicion "cantidad"
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	lista=""
	for pos in range(len(cadena)):
		if pos<cantidad:
			lista+=caracter
		else:
			lista+=cadena[pos]
	return "Su clave es "+lista

def cada_tres(cadena, cantidad):
	"""
	Dada una cadena esta funcion inserta . cada tres digitos
	modifica la cadena SOLO hasta la posicion "cantidad"
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	lista=""
	contador1=0
	contador2=0
	for pos in range(len(cadena)):
		contador1+=1
		if contador1>3 and contador2<cantidad:
			lista+="."
			contador1=1
			contador2+=1
			lista+=cadena[pos]			
		else:
			lista+=cadena[pos]			
	return lista

cadena=raw_input("Ingrese una palabra: ")
caracter=raw_input("Ingrese el caracter: ")
cantidad=int(input("Cuantas veces lo modifica: "))
#print (entre_cadena(cadena, caracter, cantidad))
#print espacios(cadena, cantidad)
#print (remplazar_caracteres(cadena, caracter, cantidad))
#print cada_tres(cadena, cantidad)