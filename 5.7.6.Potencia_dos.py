#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este cod determina si un numero ingresado espotencia de 2;
Resuleve el punto a y b de 5,7,6 del libro Algoritmos y Programacion capitulo 5 pagina 65
"""

def potencia_dos(numero):
	"""
	Resuleve si un numero es potencia de dos o no lo es.
	PARAMETRO:
		un numero entero
	RETORNO:
		el numero si es potencia de dos o cero en caso contrario
	"""
	x=1
	while (2**x)<=numero:
		if numero == (2**x):
			return numero
			break
		x+=1
	return 0


def rango(num,t):
	"""
	Dados dos numeros suma las potencias de dos en ese rango
	PARAMETRO:
		Requiere dos numeros enteros que hacen de extremos del rango
	RETORNO:
		Devuelve un entero, como suma de las pontencias en el rango
	"""
	potencia=0
	if num<t:
		while num<=t:
			potencia+=potencia_dos(num)
			num+=1
		return potencia
	else:
		while t<=num:
			potencia+=potencia_dos(t)
			t+=1
		return potencia


numero=input("Ingrese un numero: ")
t=input("Ingrese el numero del fin del rango: ")

print "La suma total de los factores de dos en el rango "+str(numero)+"<----->"+str(t)+" es: "
print rango(numero, t)
print "Incluyendo los extremos"
