#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este programa genera una matriz de tamano n, a partir de un n entero dado por 
el usuario, este programa resuelve el ejercicio 4.6.3 de libro Aprendiendo a Programar
"""

def matriz(): 
	num=input("Ingrese el tamano de la matriz: ")
	lista=[]
	for x in range(num):
		lista.append(0)

	for y in range(num):
		lista[y]=1
		lista[y-1]=0
		print lista
	return

matriz()
