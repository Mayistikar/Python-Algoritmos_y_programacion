#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este codigo utiliza una cadena de caracteres como una palabra y muestra sus caracters
del final al principio; responde el ejercicio 6.1 del libro Algoritmos y Programacion  capitulo 6 pagina 69
"""

def reverso():
	cadena=raw_input("Ingrese una cadena: ")
	for x in range(1,len(cadena)+1):
		print (cadena[-x])
	return

reverso()