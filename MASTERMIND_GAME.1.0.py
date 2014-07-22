#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Juego MASTERMIND genera un numero al azar y te permite adivinar cual es dandote 
pistas de cuantas cifras coinciden y cuantas existen;
"""
import random

def cls():
	print "\n"*100
	return

def contador(cadena, caracter):
	"""
	Determina si un caracter esta en una cadena
	PAREMTRO:
		una cadena tipo str y un caracter tipo str
	RETORANO:
		Un entero
	"""
	contador=False

	for caracteres in cadena:
		if caracter== caracteres:
			contador=True

	return contador


def azar(num_azar):

	num_azar=str(num_azar)
	num_asig=""
	coincidencia=0
	oportunidades=0

	while coincidencia!=len(num_azar):
		oportunidades+=1
		existencia=0
		coincidencia=0
		num_asig=raw_input("Que codigo propones?(**** para terminar): ")

		if num_asig=="****" or oportunidades>=20:
			print "GAME OVER!!! :("
			print "se te acabaron las oportunidades"
			print "El numero era "+num_azar
			return False
			break

		if len(num_asig)!=len(num_azar):
			while len(num_asig)!=len(num_azar):
				print "Debe ser un NUMERO de "+str(len(num_azar))+" cifras!!!"
				num_asig=raw_input("Intentalo nuevamente(**** para salir): ") 

		for cifra in range(len(num_azar)):
			if num_azar[cifra]==num_asig[cifra]:
				coincidencia+=1
			if contador(num_azar, num_asig[cifra])==True:
				existencia+=1

		print "Hay "+str(existencia)+" numeros en el codigo"'\n'
		print "Hay "+str(coincidencia)+" numeros en el lugar correcto"'\n'
		print "Te quedan "+str(20-oportunidades)+' intentos'

	print "GANASTE!!! ese era!!!"
	return True

def niveles():
	nivel=1
	salir="n"

	while nivel<=10 or salir=="q":
		num_azar=random.randrange(10**nivel,((10**(nivel+1))-1))
		num_azar=str(num_azar)
		cls()
		print "Para este nivel tendras que adivinar un numero de "+str(len(num_azar))+" cifras!!!"
		print "Buena suerte..."
		nivelx=azar(num_azar)

		if nivelx==False:
			nivel-=1
		else:
			nivel+=1

		salir=raw_input("Ingresa... q si quieres salir o ENTER para continuar...")
	
	return "EXCELENTE ACABASTE EL JUEGO... ERES EL REY"


print niveles()



