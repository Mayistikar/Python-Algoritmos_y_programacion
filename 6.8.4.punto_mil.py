#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod recibe un numero de mas de 3 digitos y los separa en sus respectivas unidades milesimas;
Resuelve el punto 6.8.4 del libro Algoritmos y Programacion capitulo 6 pagina  81
"""

def punto_mil():
	"""
	Dada una cadena esta funcion inserta . cada tres digitos en el punto mil
	PARAMETROS:
		una cadena string
	RETORNO:
		una cadena string
	"""
	lista=""
	contador=0
	cadena=raw_input("Ingrese un numero: ")

	for pos in range(len(cadena)):
		contador+=1
		if contador>3:
			lista+="."
			contador=1
			lista+=cadena[((len(cadena))-1)-pos]			
		else:
			lista+=cadena[((len(cadena))-1)-pos]
	cadena=""			
	for x in range(1,len(lista)+1):
		cadena+=lista[-x]

	return cadena

print punto_mil()