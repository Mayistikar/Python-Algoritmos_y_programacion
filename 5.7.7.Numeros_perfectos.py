#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod resuelve el punto 5.7.7 del libro algoritmos y programacion, capitulo 5, pagina 65
"""

def suma_divisores(numero):
	"""
	Encuentra la suma de divisores de un numero excluyendolo
	PARAMETRO:
		Un numero entero
	RETORNO:
		Un entero
	"""
	contador=1
	sum_divisores=0
	while contador<numero:
		if numero%contador==0:
			sum_divisores+=contador
		contador+=1
	return sum_divisores

def numeros_perfectos():
	"""
	Encuentra los primeros n numeros perfectos (que la suma de sus divisores sean iguales a el mismo)
	WARNING: no ingresar numeros mayores a 9 el bucle cierra el sistema
	"""

	n=input("Cuantos numeros quiere encontrar?")
	lista=[]
	cont=0
	while (len(lista)+1)<=n:
		if suma_divisores(cont)==cont:
			lista.append(cont)
		cont+=1
	return lista

def numeros_amgos():
	lista=[]
	n=1
	provisional=1
	while len(lista)<10:
		z=suma_divisores(n)
		if n!=z:
			y=suma_divisores(z)	
			if y==n:
				lista.append((n,z))
				provisional=z
		print lista
		print len(lista)
		if (provisional-1)==n:
			n+=2
		n+=1
	return lista
#print numeros_perfectos()
#numero=input("Ingrese un numero ")
#print suma_divisores(numero)

print numeros_amgos()


		
