#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Dada una lista de numeros este codigo devuelve cuales son primos, la sumatoria 
de los mismos, el promedio y el factorial de cada numero.
Resuelve el punto 7.6.5 del libro Algoritmos y programacion del capitulo 7 pagina 98
"""


"------------------FUNCIONES DE APOYO-----------------------"

def primo(num1):
	"""
	Determina si un numero es primo
	PARAMETROS:
		un entero
	RETORNO:
		retorna el numero si es  primo o falso en caso contrario
	"""
	for x in range (1,num1):
		if (num1%x==0 and x!=num1 and x!=1):
			return False
	return num1


def factorial(n1):	# Esta es una funcion de apoyo
	"""
	Imprime una string con el factorial de un numero
	PARAMETROS:
		Un numero entero
	RETORNO:
		Un cadena string con el factorial del numero
	"""

	count=1
	t=n1
	z=[str(t)]
	cad=""
	for x in range (1,t+1):
		count*=x
		t-=1
		if t!=0:
			z.append("*")
			z.append(str(t))
	for pet in z:	# Esta linea limpia la lista z para volver un resultado legible
		cad+=pet

	return cad	


"---------------FUNCIONES PRINCIPALES-----------------"

def lista_primos(lista):
	"""
	Desde una lista de numeros recoge solo los numeros primos
	PARAMETROS:
		Una lista de numeros
	RETORNO:
		Una nueva lista con solo numeros primos
	"""

	new=[]
	for numero in lista:
		var=primo(numero)
		if var!=False:
			new.append(var)
	return new

def suma_promedio(lista):
	"""
	Determina la sumatoria y el promedio de una lista de numeros
	PARAMETROS:
		Una lista
	RETORNO:
		Un tupla con dos elementos, la sumatoria y el promedio
	"""

	sumatoria=0
	contador=0
	for numero in lista:
		sumatoria+=numero
		contador+=1
	promedio=sumatoria/float(contador)
	return sumatoria, promedio

def factorial_lista(lista):
	"""
	Imprime una lista con los factoriales de cada numero en una lista
	PARAMETROS:
		Una lista
	RETORNO:
		Un una lista con cadenas string con los factorial de cada numero
	"""

	new_fact=[]
	for num in lista:
		new_fact.append(factorial(num))
	return new_fact


	

lista=[1,2,3,4,5,6,7,8,9]
tupla=('z','d','f','h','y','r','t','c','z','v','b')
arreglo=sorted(tupla)
print lista_primos(lista)
print suma_promedio(lista_primos(lista))
print factorial_lista(lista_primos(lista))
print "++++++++++++++++++++++++++++++++++++"
print tupla
print arreglo
print 