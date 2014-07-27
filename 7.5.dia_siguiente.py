#!/usr/bin/env python
#-*-coding: utf-8-*-

"""
Dadas dos una tupla con una fecha formato dia,mes,ano, calcula cual es el dia siguiente;
Resuelve el punto 7.5 del libro Algoritmos y programacion del capitulo 7 pagina 86
"""

def dia_siguiente(fecha):
	"""
	Teniendo una fecha formato (d,m,a) en una tupla muestra cual es el dia siguiente
	PARAMETRO:
		Una tupla con una fecha con enteros en cada elemento tipo (12,10,98)
	RETORNO:
		Una tupla con la fecha siguiente
	"""

	dia_s=fecha[0]+1
	mes_s=fecha[1]
	ano_s=fecha[2]

	if mes_s==02 and dia_s>28:
		dia_s=1
		mes_s+=1
	elif dia_s>30:
		dia_s=1
		mes_s+=1
		if mes_s>12:
			mes_s=1
			ano_s+=1
	fecha=(dia_s,mes_s,ano_s)

	return fecha

fecha=input("Ingrese una fecha con formato (dia,mes,ano): ")
print "El dia siguiente es "+str(dia_siguiente(fecha))
	

