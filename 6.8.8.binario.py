#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Recibe una cadena binaria de unos y ceros y devuelve su numero correspondiente;
Resuelve la estancia 6.8.8 del libro Algoritmos y Programacion  capitulo 6 pagina 82
"""

def binario(cadena):
	"""
	Esta funcion convierte un numero binario a un numero entero
	PARAMETROS:
		Una cadena string
	RETORNO:
		Un numero entero
	"""
	binario="0b"
	binario+=cadena
	var=int(binario,2)
	return var


cadena=raw_input("Ingrese su numero binario: ")
print "Su numero entero es: "
print binario(cadena)
