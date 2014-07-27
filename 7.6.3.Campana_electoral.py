#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Resuelve el punto 7.6.3 del libro Algoritmos y programacion del capitulo 7 pagina 98
"""

def estimado(tupla):
	"""
	Imprime un mensaje para todos los elementos de la tupla
	"""
	for nombre in tupla:
		if nombre[1]=='M':
			print "Estimado "+str(nombre[0])+" Vote por mi!"
		else:
			print "Estimada "+str(nombre[0])+" Vote por mi!"

def vectores(tupla, origen, cantidad):
	"""
	Imprime un mensaje utilizando los elements de la tupla, un numero "origen" que determina de donde
	empieza a usar los elementos y un numero 'cantidad' que determina cuantos elemento usar apartir de alli
	PARAMETROS:
		Una tupla, dos enteros
	RETORNO:
		Un cadena con un mensaje para el usuario
	"""

	if (origen-1)>len(tupla) or ((origen-1)+cantidad)>len(tupla):
		print "Datos de origen o cantidad erroneos"
	else:
		for pos in range((origen-1), (origen-1+cantidad)):
			if tupla[pos][1]=='M':
				print "Estimado "+str(tupla[pos][0])+" Vote por mi!"
			else:
				print "Estimada "+str(tupla[pos][0])+" Vote por mi!"
			

tupla=(("carlos","M"), ("Julian","M"), ("Margarita","F"), ("Mario","M"), ("Fernando","M"))
origen=int(input("Determine el origen: "))
cantidad=int(input("Determine la cantidad de nombres: "))

estimado(tupla)
print "++++++++++++++++"
vectores(tupla, origen, cantidad)