#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
De una cadena devuelve una lista y cuantas palabras de mas de 5 letras tiene
	
"""

def tolist(cadena):
	"""
	Esta funcion toma una cadena y la convierte en lista para luego contar los caracteres de cada elemento
	y si en total son 5 lo contabiliza
	PARAMETROS:
		Una lista
	RETORNO:
		Un mensaje al usuario con la cantidad de elementos con 5 caracteres hay en la lista
	"""
	contador1=0
	c=cadena.split()
	for x in c: 	#Recorre cada elemento
		contador=0
		for j in x: 	#Recorre cada caracter de cada elemento
			contador+=1		#Contabiliza los caracteres
		if contador==5: 	#Si el total de caracteres es 5 lo contabiliza
			contador1+=1	#Contabiliza los elementos con 5 caracteres
			
	return "Esta cadena tiene "+str(contador1)+" palabras de 5 letras"

string="Esta cadena tiene varias palabras de cinco letras"
print tolist(string)