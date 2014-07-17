#!/user/bin/env python
#-*-coding:utf-8;-*-

"""Un programa que dado unos parametros resuelve distintos problemas
resuelve el punto 3.8.4 de Algoritmos y Programacion"""

def norma():
	"""Dados los pts de origen de un vector calcula su norma"""

	x=input("Cual es el origen en X: ")
	y=input("Cual es el origen en y: ")
	pi=((x**2)+(y**2))**(1/2)
	print "La norma del vector es igual a: "+str(pi)
	return pi

def resta_plano():
	"""Dados dos pts de un plano los resta"""

	print "Determine los valores en X y Y del plano""\n"
	x1=input("El punto en X1 es: ")
	y1=input("El punto en Y1 es: ")
	x2=input("El punto en X2 es: ")
	y2=input("El punto en y2 es: ")
	difx=x2-x1
	dify=y2-y1
	print "la resta en X y Y respectivamente es: "+str(difx)+" y "+str(dify)
	return dify, difx

def dist_plano():
	"""Dados dos pts en un plano, encuentra su distancia"""

	lista=resta_plano()
	num=lista[0]/lista[1]
	float(num)
	print "La distancia entre los puntos es: "+str(num)
	return num

print norma()
print 
print resta_plano()
print 
print dist_plano()

	

	







