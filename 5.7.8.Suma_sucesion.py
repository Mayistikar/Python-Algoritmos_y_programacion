#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod pide al usuario una sucesion de numeros naturales, y devuelve la suma de dicha sucesion:
Resuelve el punto 5.7.8 del libro Algoritmos y Programacion capitulo 5 pagina 66
"""

def suma_sucesion(suc):
	lista=[]
	contador=0.0
	suma=0
	while suc>=0:
		suma+=suc
		lista.append(suc)
		suc=input("Ingrese el siguiente numero de la sucesion (ingrese -1 para terminar): ")
		contador+=1
	promedio=suma/contador
	print "Los numeros listados son: "+str(lista)
	print '\n'"La suma total es "+str(suma)+" y su promedio es: "+str(promedio)
	return 

suc=input("Ingrese un numero de la sucesion: ")
suma_sucesion(suc)