#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Resuelve la estancia 6.8.5 del libro Algoritmos y Programacion  capitulo 6 pagina 69
"""

def primera_letra(cadena):
	"""
	Esta funcion muestra la primera letra de cada palabra
	PARAMETROS:
		Una cadena string
	RETORNO:
		Una cadena string
	"""
	lista=cadena[0]
	for x in range(len(cadena)):
		if cadena[x]==" " and (x+1)< len(cadena):
			lista+=cadena[(x+1)]
	return lista

def primera_mayusculas(cadena):
	"""
	Esta cadena pone la primera letra de cada palbrab con mayusculas
	PARAMETROS:
		Una cadena string
	RETORNO:
		Una cadena string
	"""
	lista=""
	lista=cadena[0].upper()
	for x in range(1,len(cadena)):
		if cadena[x-1]==" ":
			lista+=cadena[x].upper()
		else:
			lista+=cadena[x]

	return lista

def palabras_conA(cadena):
	"""
	Devuelve cada palabra que empieze con A en una frase
	PARAMETROS:
		Una cadena string
	RETORNO:
		Una cadena string
	"""
	cadenax=" "+cadena
	lista=" "
	for pos in range(len(cadenax)):
		if (cadenax[pos]=='a' or cadenax[pos]=='A') and (cadenax[pos-1]==" "):
			for posj in range(pos,len(cadenax)):
				if cadenax[posj]==" ":
					break
				else:
					lista+=cadenax[posj]
			lista+=" "
	return lista

	
cadena=raw_input("Ingrese una frase: ")

#print (primera_mayusculas(cadena))
#print (primera_letra(cadena))
print palabras_conA(cadena)