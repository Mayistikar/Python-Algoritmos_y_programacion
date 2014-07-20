#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo;
Este codigo resuelv el  punto 5.7.9 del libro Algoritmos y programacion capitulo 5 pagina 66
"""

def multiplos_for(a,b):

	for x in range(b):
		multiplo=a*x
		if multiplo>=b:
			break
		lista.append(multiplo)
	return lista

def multiplos_while(a,b):
	multiplo=0
	contador=0
	while multiplo<b:
		lista.append(multiplo)
		contador+=1
		multiplo=a*contador
	return lista



lista=[]
a=input("Ingrese un numero: ")
b=input("Ingrese el segundo numero ")
print multiplos_while(a,b)
