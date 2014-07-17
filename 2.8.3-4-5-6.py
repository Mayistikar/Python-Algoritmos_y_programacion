#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""Este programa hace la conversion de grados Fahrenheit a Celsius"""
def conversion(x):
	return str(x)+" Equivale a: "+str((x-32)*(5.0/9.0))+" En Celsius" #Tener cuidado con la fraccion
	#debe usarse floats

def tabla(): # Resuelve el problema del punto 2.8.4
	for grado in range(0,121):
		if grado%10==0:
			print conversion(grado)
	return

def pares():	#esta resuleve el problema del punto 2.8.5
	print "Defina dos numeros de lista "
	z1=input("Entre: ")
	z2=input("y ")
	print "los pares de esta lista son: "
	for x in range(z1,(z2+1)):
		if x%2==0:
			print x
	return

def triangulares(n):	#Esta funcion resuelve el problema del punto 2.8.6
	z=1
	for x in range(1,n+1):
		print str(x)+" - "+str(z)
		z+=x+1
	print "\n""*******Otra manera******""\n"
	for z in range (1,n+1):
		print str(z)+" - "+str(z*(z+1)/2)
	return 


#fah=input("Ingrese la temperatura en Fahrenheit: "
#tabla()	
#pares()
num=input("Ingrese su numero ")
triangulares(num)





