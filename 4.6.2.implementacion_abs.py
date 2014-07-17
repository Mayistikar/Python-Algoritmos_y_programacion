#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este programa es una implementacion propia de la funcion abs() que devuelve
el valor absoluto de un numero-----Esto es la solucion al ejercicio 4.6.2 del libro Algoritmos 
y programacion +++ capitulo4 +++ pagina 55
"""

print "\n""BIENVENID@ A SU HERRAMIENTA DE VALOR ABSOLUTO""\n"

def absoluto(num):
	"""
	FUNCION:
		Esta funcion determina el valor absoluto de un numero
	PARAMETROS: 
		recibe un numero cualquiera 
	RETORNA:
		el valor absoluto del numero
	"""

	if num<0:
		return (num*(-1))
	elif not num:
		return num
	else:
		return num

x=input("Ingrese el numero a evaluar: ")
print "\n""El valor absoluto del numero es: "

print absoluto(x)


