#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Recibe una tupla y determina si esta o no ordenada;
Resuelve el punto 7.6.1 del libro Algoritmos y programacion del capitulo 7 pagina 98.
"""

def ordenada(tupla):
	contador=0
	orden=sorted(tupla)
	for pos in range(len(tupla)):
		if tupla[pos] ==  orden[pos]:
			contador+=1
		if contador==len(tupla):
			return "Esta ordenada de menor a mayor"

	return "Esta tupla no esta ordenada"

tupla=(2,1,4,7,6,3,5)
print ordenada(tupla)




