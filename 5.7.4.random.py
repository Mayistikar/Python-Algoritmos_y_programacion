#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este codigo genera un numero al azar y te permite adivinarlo dandote pistas;
Resuelve el punto 5.7.4 del libro Algoritmos y Programacion capitulo 5 pagina  65
"""
import random	
def adivinar():
	print "BIENVENID@ A ADIVINA TU NUMERO""\n"
	opcion="a"
	numero=random.randrange(1,90)
	while opcion!=numero:
		opcion=input("Ingrese el posible numero: ")
		if opcion==numero:
			print "Bravo Ganaste ese era!!!"
			break
		elif opcion>numero:
				print "casi pero te pasaste... intenta con otro mas peque!!!"
		elif opcion<numero:
				print "No te falta casi nada... es un poco mas grande!!!"
		else:
			print "Que estas escribiendo???"

adivinar()
