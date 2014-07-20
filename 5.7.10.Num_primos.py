#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod recibe un numero natural e imprime todos los numeros primos hasta ese numero;
Resuelve el punto 5.7.10 del libro Algoritmos y Programacion del capitulo 5 de la pagina 66
"""

def primo(num1):
	"""
	Determina si un numero es primo
	requiere como parametro un entero
	retorna el numero si es  primo o falso en caso contrario
	"""
	for x in range (1,num1):
		if (num1%x==0 and x!=num1 and x!=1):
			return False
	return num1

def lista_primos(num2):
	"""
	Esta funcion crea una lista de numeros primos entre 1 y un numero entero
	PARAMETRO:
		un numero entero
	RETORNA:
		Una lista con numeros primos
	"""
	for x in range(2,num2+1):
		if primo(x)!=False:
			lista.append(x)
	return lista

lista=[1]
num2=input("Hasta que numero le calculamos? ")
print lista_primos(num2)