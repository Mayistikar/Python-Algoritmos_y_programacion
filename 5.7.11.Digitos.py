#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Determina si un digito escogido esta en la notacion de un numero natural definido;
Resuelve el punto 5.7.11 del libro Algoritmos y Programacion del capitulo 5 pagina 66
"""

def encuentra_digito(d,n):
	contador=0
	lista=n
	while contador<(len(lista)):
		if d == lista[contador]:
			print "El digito si se encuentra en el numero...""\n"
			print "En la posicion "+str(contador+1)+" de izquierda a derecha"
			return 
			break
		contador+=1
	print "El digito no se encuentra en el numero especificado"
	return

d=raw_input("Ingresa un digito entre 0 y 9: ")
n=raw_input("Ingresa un numero natural cualquiera: ")
lista=[]
encuentra_digito(d, n)
