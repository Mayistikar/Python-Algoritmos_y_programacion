#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este soft pide un numero positivo al usuario y se repite hasta que lo haga;
Resolvemos el ejercicio 5.3 del libro Algoritmos y Programacion Capitulo 5 pagina 63

"""

def positivo():
	"""
	Ciclo indefinido
	"""
	numero=-2
	while numero<0:
		numero=input("Ingrese un numero positivo: ")

def positivo1():
	"""
	Ciclo Interactivo
	"""
	confir="s"
	while confir=="S" or confir=="s":
		numero=input("Ingresa un numero positivo: ")
		if numero<0:
			print "Su numero es negativo..."
			confir=raw_input("Quieres continuar S/N: ")

def positivo2():
	"""
	Ciclo con centinela
	"""
	numero=raw_input("Ingrese un numero ("+"*"+" para salir): ")
	while numero<>"*":
		numero=int(numero)
		if numero>0:
			print "Su numero es positivo"
		elif numero==0:
			print "Su numero es cero"
		else:
			print "Su numero es negativo"
		numero=raw_input("Ingrese un numero ("+"*"+" para salir): ")

def positivo3():
	"""
	Ciclo con Break
	"""
	while True:
		numero=input("Ingrese un numero positivo: ")
		if numero>0:
			print "Su numero es positivo"
			break
		elif numero==0:
			print "Su numero es cero"
		else:
			print "Su numero es negativo"

positivo3()			
positivo2()
positivo()
positivo1()


