#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Resuelve el punto 6.8.6. del libro Algoritmos y Programacion\capitulo 6\pagina 81
"""
def solo_consonantes(cadena):
	"""
	Dada una cadena devuelve solo consonantes
	PARAMETROS:
		Cadena tipo string
	RETORNO:
		Cadena tipo string
	"""
	lista=""
	for pos in cadena:
		if pos=='a' or pos=="e" or pos=="i" or pos=="o" or pos=="u"  or pos=="A" or pos=="E" or pos=="I" or pos=="O" or pos=="U":
			pass
		else:
			lista+=pos
	return lista

def solo_vocales(cadena):
	"""
	Dada una cadena devuelve solo vocales
	PARAMETROS:
		Cadena tipo string
	RETORNO:
		Cadena tipo string
	"""
	lista=""
	for pos in cadena:
		if pos=='a' or pos=="e" or pos=="i" or pos=="o" or pos=="u"  or pos=="A" or pos=="E" or pos=="I" or pos=="O" or pos=="U":
			lista+=pos
		else:
			pass
			
	return lista

def por_siguiente(cadena):
	"""
	Dada una cadena devuelve solo vocales
	PARAMETROS:
		Cadena tipo string
	RETORNO:
		Cadena tipo string
	"""
	lista=""
	for pos in cadena:
		if pos=='a' or pos=='A':
			lista+='e'
		elif pos=='e' or pos=='E':
			lista+='i'
		elif pos=='i' or pos=='I':
			lista+='o'
		elif pos=='o' or pos=='O':
			lista+='u'
		elif pos=='u' or pos=='U':
			lista+='a'
		else:
			lista+=pos
	return lista

def palindromo(cadena):
	"""
	Dada una cadena determina si es un palindromo
	PARAMETROS:
		Cadena tipo string
	RETORNO:
		Cadena tipo string
	"""
	lista=""
	contador=0

	for letra in cadena:
		if letra!=" ":
			lista+=letra

	for pos in range(len(lista)):
		if lista[pos]==lista[len(lista)-1-pos]:
			contador+=1
			if contador==len(lista):
				return cadena+" Es un palindromo"
	return cadena+" No es un palindromo"


cadena=raw_input("Ingrese una frase: ")
#print (solo_consonantes(cadena))
#print (solo_vocales(cadena))
#print (por_siguiente(cadena))
print (palindromo(cadena))
