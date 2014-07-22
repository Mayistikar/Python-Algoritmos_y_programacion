#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod recorre una cadena en busca de un caracter cuenta las veces que este esta en la cadena;
Compara cuantas veces se encuentran dos caracteres en una cadena y dice cual es mayor;
Resuelve el punto 6.4-5. de libro Algoritmos y Programaicon\capitulo 6 pagina 73
"""

def contador(cadena, caracter):
	"""
	Determina cuantas veces esta un caracter en una cadena
	PAREMTRO:
		una cadena tipo str y un caracter tipo str
	RETORANO:
		Un entero
	"""
	contador=0
	for caracteres in cadena:
		if caracter== caracteres:
			contador+=1

	return contador

def comparador(cadena, caracter1, caracter2):
	"""
	pide la cantidad de caracteres que hay en una cadena usando (def contador) y determina cual caracter es mayor;
	PARAMETROS:
		cadena en str, caracter1 en str y caracter2 en str
	RETORNA:
		La cantidad de veces que esta caracter1 y caracter2 respectivamente
	"""
	
	contador1=contador(cadena, caracter1)
	contador2=contador(cadena, caracter2)
	if contador1==0 and contador2==0:
		print ("Ninguno de los dos caracteres se encuentran")
	elif contador1 > contador2:
		print ("El caracter: "+caracter1+" se encuentra as veces que "+caracter2)
	elif contador1 < contador2:
		print ("El caracter: "+caracter2+" se encuentra as veces que "+caracter1)
	else:
		print ("Los dos caracteres estan la misma cantidad de veces")

	print ("Los caracteres: "+caracter1+" y "+caracter2+" Se ecuentran(respectivamente): ")
	return contador1, contador2

cadena=raw_input("Ingresa la palabra: ")
caracter1=raw_input("Ingresa el caracter1 a buscar: ")
caracter2=raw_input("Ingresa el caracter2 a buscar: ")

print comparador(cadena, caracter1, caracter2)
#print contador(cadena, caracter)