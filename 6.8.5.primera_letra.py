#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Resuelve la estancia 6.8.5 del libro Algoritmos y Programacion  capitulo 6 pagina 69
"""

def primera_letra(cadena):
	lista=cadena[0]
	for x in range(len(cadena)):
		if cadena[x]==" " and (x+1)< len(cadena):
			lista+=cadena[(x+1)]
	return lista

def primera_mayusculas(cadena):
	lista=""
	lista=cadena[0].upper()
	for x in range(1,len(cadena)):
		if cadena[x-1]==" ":
			lista+=cadena[x].upper()
		else:
			lista+=cadena[x]

	return lista

def palabras_conA(cadena):
	lista=""
	espacio=0
	for x in range(len(cadena)):
		if cadena[-x]==" ":
			espacio=x
		if (cadena[-x]=='a' or cadena[-x]=='A') and ((cadena[-(x+1)]==" ") or cadena[-x]==cadena[0]):
			for pos in range(((len(cadena))-(x+1)),((len(cadena)-1)-espacio)):
				lista+=cadena[pos]
			lista+=" "				
					
	return lista



cadena=raw_input("Ingrese una frase: ")

#print (primera_mayusculas(cadena))
#print (primera_letra(cadena))
print palabras_conA(cadena)