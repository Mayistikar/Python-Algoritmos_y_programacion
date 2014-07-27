#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Crea una tupla con una representacion de las cartas de la baraja;
Resuelve la estancia 7.3 del libro Algoritmos y Programacion  capitulo 7, pagina 86
"""

cards=("2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah","2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac","2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As","2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad")


def pkr(*krts):
	"""
	Recibe una tupla con 5 cartas y determina si hay un poker en ellas
	PARAMETRO:
		tupla con 5 elementos
	RETORNO:
		un string diciendo si es poker (Modificable)
	"""
	x=0					#Variables
	num_card=krts[0][0] #variables
	contador=0			#variables
	while x<5:

		if num_card==krts[x][0]: #determina si en el caracter [0] del elemento [x] de la tupla hay coincidencia
			contador+=1			 #Cuenta las coincidencias
			num_card=krts[x][0]	

		if contador==3:			#verifica las coincidencias
			return "Es poker"
		x+=1

print pkr("2h", "2d", "2s", "4s", "2c")









