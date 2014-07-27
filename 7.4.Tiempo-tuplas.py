#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Determina una representacion del tiempo usando tuplas
Resuelve el punto 7.4 del libro Algoritmos y programacion del capitulo 7 pagina 86
"""

tiempo=("horas","minutos","segundos")

def suma_tiempo(tiempo1, tiempo2):
	"""
	Dadas dos tuplas con tiempo en formato (h/m/s) retorna la suma de ellos
	PARAMETROS:
		Dos tuplas con numeros tipo (12,13,14)
	RETORNO:
		La suma de las dos tuplas en int
	"""

	time1=(tiempo1[0]*3600)+(tiempo1[1]*60)+tiempo1[2]
	time2=(tiempo2[0]*3600)+(tiempo2[1]*60)+tiempo2[2]

	return time1+time2

tiempo1=input("Ingresa un tiempo con formato h/m/s: ") #Recibe una tupla en formato tipo  (12,13,14)
tiempo2=input("Ingresa un tiempo con formato h/m/s: ")	#Recibe una tupla en formato tipo  (12,13,14)

print "La suma de los tiempos en segundos es: "+str(suma_tiempo(tiempo1, tiempo2))






