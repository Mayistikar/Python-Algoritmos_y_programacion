#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""Este soft permite hacer distintos calculos geometricos a medida de peticion de usuario"""

def rectangulo():	#esta funcion calculoa el perimetro y el area de un rectangulo con su base y area
	b=input("escribe la base del rectangulo: ")
	h=input("cual es su altura: ")
	per=(2*b)+(2*h)
	area=b*h
	return "el perimetro es: "+str(per)+" y el area es: "+str(area)

def circulo():
	r=input("El radio del circulo es: ")
	per=2*3.1415*r
	area=3.1415*(r**2)
	return "el perimetro es: "+str(per)+" y el area es: "+str(area)

def esfera():
	r=input("El radio de la esfera: ")
	vol=(4/3)*(3.1415)*(r**3)
	return "el volumen de la esfera es: ", vol

def rectcoord():
	x1=input("Ingresa la coordenada x1")
	x2=input("Ingresa la coordenada x2")
	y1=input("Ingresa la coordenada y1")
	y2=input("Ingresa la coordenada y2")
	area=(x2-x1)*(y2-y1)
	return area

def pitagoras():
	cat1=input("Ingresa los catetos del triangulo: ")
	cat2=input("Ingresa los catetos del triangulo: ")
	hipo=((cat1*2)+(cat2*2))**(1/2)
	return "la hipotenusa es: "+str(hipo)
	

print "**ESCRIBE EL INDICE DE LA OPERACION QUE QUIERAS**""\n"
print "************************************************" "\n"
print "(1) Calcula el perimetro y el area de un RECTANGULO"
print "(2) Calcula el perimetro y el area de un circulo"
print "(3) Calcula el volumen de una esfera"
print "(4) Calcula el area de un RECTANGULO desde sus COORDENADAS"
print "(5) Calcula la hipotenusa de un triangulo""\n"
var=input("Escoje tu opcion: ")
if var==1:
	print rectangulo()
elif var==2:
	print circulo()
elif var==3:
	print esfera()
elif var==4:
	print rectcoord()
elif var==5:
	print pitagoras()
else:
	print "No entiendo tu peticion"


