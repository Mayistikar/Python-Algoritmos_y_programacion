#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Programa de telegramas... brinda el costo y el mensaje
esuelve el punto 7.10 del libro Algoritmos y programacion del capitulo 7 pagina 95
"""

def telegrama(cadena, preciopl, preciopc, longitud):
	new=""
	cont=0
	costo=0
	lista=cadena.split()
	for palabra in lista:

		for x in range(len(palabra)):
			new+=palabra[x]
			if x>longitud:
				new+="@"
				costo+=preciopl

		lista[cont]=new
		cont+=1
		costo+=preciopc

	return lista

cadena=raw_input("Ingrese su oracion: ")
preciopc=int(input("Ingrese el precio de la palabra corta: "))
preciopl=int(input("Ingrese el precio de la palabra larga: "))
longitud=int(input("Ingrese la longitud de la palabra: "))


print telegrama(cadena, preciopl, preciopc, longitud)
