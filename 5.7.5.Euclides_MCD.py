#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod encuentra los maximos comunes divisores de dos numeros siguiendo el algoritmo de Euclides
"""

def divisiores():
	n=input("Ingrese el primer numero: ")
	m=input("Ingrse el segundo numero: ")

	r=m%n
	while r!=0:
		m=n
		n=r
		r=m%n

	print "El MCD de los numeros es: "
	return n


print divisiores()