#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""Este programa hace lo que pida el usuario derivado de opciones"""

def operadores():
	n1=input("ingresa un numero: ")
	n2=input("Ingresa el segundo numero: ")
	suma=n1+n2
	resta=[n1-n2, n2-n1]
	mul=n1*n2
	div=[n1/n2, n2/n1]
	return suma, resta, mul, div

def tabmultiplicar():
	n1=input("ingresa un numero: ")
	print "\n""SU TABLA DE MULTIPLICAR ES:""\n"
	for x in range(0,10):
		print str(n1)+" x "+str(x)+" = "+str(n1*x)

def factorial():
	n1=input("ingrese su numero: ")
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

print "\n""QUE DESEA HACER...""\n"
print "(1) Operar dos numeros"
print "(2) La tabla de MULTIPLICAR un numero"
print "(3) EL factorial de un numero""\n"
var=input("Escriba su opcion... ")

if var==1:
	print operadores()
elif var==2:
	tabmultiplicar()
elif var==3:
	print factorial()
else:
	print "No entiendo su peticion"










