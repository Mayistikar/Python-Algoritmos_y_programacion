#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Este soft recibe un numero entero y lo descompone en sus factores primos:
Resuelve el punto 5.7.2. del libro Algoritmos y Programacion capitulo 5 pagina 65
"""

lista=[]
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
	for x in range(2,num2):
		if primo(x)!=False:
			lista.append(x)
	return lista

def divisible(lista,num3):
	"""
	Dada una lista de numeros esta funcion encuentra si un numero z es divisible por alguno de la lista_primos
	"""
	for numero in lista:
		if num3%numero==0:
			factores.append(numero)
	return factores

def factores_x(lista, numero, factores_finales):
	"""
	Esta funcion permite realizar el calculo de los factores primos de un numero
	PARAMETROS:
		requiere de dos listas vacias y el numero a calcular
	RETORNA:
		Una lista con los factores del numero
	"""
	divisibles=[]
	print "++++++++++++++++++++++++"
	print "Sus factores primos son: "
	print "++++++++++++++++++++++++"

	while True:
		salida1=primo(numero)
		if salida1!=False:
			factores_finales.append(salida1)
			break

		else:
			lista_primos(numero)	#Trae una lista con los numeros primos entre 1 y el NUMERO
			divisibles=divisible(lista, numero) #trae una lista con los primos divisores del NUMERO

			factores_finales.append(divisibles[len(divisibles)-1])
			numero=numero/divisibles[len(divisibles)-1]
	return factores_finales
		



factores_finales=[1]
lista=[]
factores=[]
numero=input("Ingrese un numero: ")
print factores_x(lista, numero, factores_finales)






