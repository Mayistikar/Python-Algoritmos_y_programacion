#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""Este programa resuelve el punto 3.8.3 del libro Algoritmos y programacion"""

def mayor_mult():
	"""Dados cuatro numeros retorna la multiplicacion mayor entre dos de ellos"""	
	lista=[]
	for posicion in range(4):
		z=input("Ingrese uno de los numeros para la cuenta: ")
		t=abs(z)
		lista.append(t)

	lista.sort()
	mayor=lista[3]
	mayor*=lista[2]

	return mayor

print mayor_mult()