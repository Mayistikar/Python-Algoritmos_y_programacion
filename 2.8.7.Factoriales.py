#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""Este Programa calcula factoriales de numeros ingresados"""

def factorial(n1):	# Esta es una funcion de apoyo
	count=1
	t=n1
	z=[str(t)]
	cad=""
	for x in range (1,t+1):
		count*=x
		t-=1
		if t!=0:
			z.append("*")
			z.append(str(t))
	for pet in z:	# Esta linea limpia la lista z para volver un resultado legible
		cad+=pet

	print "el fac de: "+str(n1)+" es: "+cad+" = "+str(count)
	return "\n"	


def factoriales(): # Esta funcion resuelve el problema
	m=input("Cuantos valores va a ingresar: ")
	n=input("Ingrese un valor: ")
	print factorial(n)
	for x in range(1,m):
		n=input("Ingrese otro valor: ")
		print factorial(n)
	return

factoriales()


