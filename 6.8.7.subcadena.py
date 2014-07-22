#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Dada una cadena y una subcadena revisa si la subcadena se encuentra en la cadena;
Resuelve el punto 6.8.7. del libro Algoritmos y Programacion\capitulo 6\pagina 82

"""

def subcadenax(cadena, subcadena):
	"""
	Dada una cadena y una subcadena revisa si la subcadena se encuentra en la cadena;
	PARAMETROS:
		Requiere dos cadenas tipo string
	RETORTA: 
		Una cadena string
	"""
	contador=0
	x=0
	for pos in range(len(cadena)):
		if cadena[pos]==subcadena[x]:
			if cadena[pos+1]==subcadena[x+1]:
				x+=1
				contador+=1
		if contador==(len(subcadena)-1):
			return "Es una subcadena"
			break
		else:
			pass
	
	return "No es una subcadena"

def orden_alfab(cadena):
	"""
	Dada una cadena y una subcadena revisa si la subcadena se encuentra en la cadena;
	PARAMETROS:
		Requiere dos cadenas tipo string
	RETORTA: 
		Una cadena string
	"""
	cadena+=" "
	lista=""
	orden=[]
	for x in range(len(cadena)):
		if cadena[x]!=" ":
			lista+=cadena[x]
		else:
			orden.append(lista)
			lista=""
	orden.sort()
	return orden
	

#cadena=raw_input("Ingrese una cadena: ")
#subcadena=raw_input("Ingrese una subcadena: ")
oracion=raw_input("Ingrese una lista de palabras: ")
#print subcadenax(cadena, subcadena)
print orden_alfab(oracion)