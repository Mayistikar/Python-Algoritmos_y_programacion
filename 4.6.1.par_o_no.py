#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este programa resuelve el ejercicio 4.6.1 del libro Algoritmos y programacion en pagina 55

"""

print "\n""BIENVENID@ A SU HERRAMIENTA PARA DETERMINAR PARES Y PRIMOS""\n"

def primo_no_primo(x):

	for numeros in range(2,(x-1)):

		if x%numeros==0 and numeros!=x:
			print "El numero NO es primo!"
			break
		else:
			print "El numero es primo!"
			break

	return 

def par_no_par():
	x=input("Ingrese el numero a evaluar: ")

	if x%2==0:
		print "El numero es par"
	else:
		print "El numero no es par"
	return x


num=par_no_par()
print 
primo_no_primo(num)

