#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""Este programa recibe un nombre y lo saluda"""

def saludo():
	nombre=raw_input("Cual es tu nombre? ")
	print "Hola! "+nombre+" Como estas? :)""\n"
	print "Dame dos numeros... "
	n1=input("el primero es? ")
	n2=input("el segundo es? ")
	print
	print "el producto de los dos es: "
	print n1*n2
	return
saludo()