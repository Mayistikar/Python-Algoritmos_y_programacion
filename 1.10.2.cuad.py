#!/usr/bin/env python
#!-*-encoding:utf-8;-*_
#Este programa calcula el cuadrado de un numero

print "BIENVENID@ A SU PROGRAMA CUADRADOS"+"\n"

def cuad():
	"""esta funcion llama dos numeros para un rango e imprime sus cuadrados"""
	n1=input("Ingrese el primer numero: ")
	n2=input("Ingrese el segundo numero: ")
	print 
	for numero in range (n1,n2):# es importante tener en cuenta que python empieza sus indices en 0 y no en 1
		print numero
		print numero**2 ## tambien se puede usar numero*numero
		print "*********"
	print"Ok... te espero luego"
	return

cuad()


