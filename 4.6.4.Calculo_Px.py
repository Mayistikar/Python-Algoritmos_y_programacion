#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este programa resuelve distinto problemas de calculo obteniendo datos del usuario;
con ello resolvemos el punto 4.6.4 del libro Algoritmos y programacion Capitulo 4 pagina 55
"""

def max_min():
	"""
	Esta funcion permite calculoar el maximo o minimo de un polinomio cuadratico
	a partir de sus coeficientes a b y c
	PARAMETROS:
	RETORNA:
		es maximo o es minimo en un string
	"""
	x=0.0
	y=0.0
	print "\n""Tenemos un polinomio ax^2 + bx + c""\n"
	a=input ("Ingrese el valor para a ")
	float(a)
	b=input ("Ingrese el valor para b ")
	float(b)
	c=input ("Ingrese el valor para c ")
	float(c)

	x=((-b)/(2*a))
	y=(a*(x**2))+(b*x)+c


	if y>0:
		return "Solo tienen un maximo: "+str(x)+" Con coordenadas ("+str(x)+","+str(y)+")"
	else:
		return "Solo tienen un minimo: "+str(x)+" Con coordenadas ("+str(x)+","+str(y)+")"

def raices():
	"""
	Esta funcion calcula las raices de un polinomio cuadrado y las muestra exceptuando las raices
	complejas
	"""
	x=0
	y=0
	print "\n""Tenemos un polinomio ax^2 + bx + c""\n"
	a=input ("Ingrese el valor para a ")
	float(a)
	b=input ("Ingrese el valor para b ")
	float(b)
	c=input ("Ingrese el valor para c ")
	float(c)
	if a==0:
		return "No es un polinomio cuadratico"
	else:
		y=((b**2)-(4*a*c))

	if y<0:
		return "El polinomio solo tiene raices IMAGINARIAS" 
	else:
		x=((-b)+(((b**2)-(4*a*c))**(1/2)))/(2*a)
		
	return "Sus raices son: "+str(x)+","+str(-x)

def recta():
	"""
	Dados la pendiente y punto de origen de dos rectas
	calculamos el punto de interseccion entre estas
	"""
	print "\n""Por favor ingresar datos de las rectas""\n"
	m1=input("La pendiente de la Recta 1 es: ")
	(x1,y1)=input ("Por favor ingrese el origen de la Recta 1 --- tipo --- x,y --> 2,5 --> ")
	m2=input("La pendiente de la Recta 2 es: ")
	(x2,y2)=input ("Por favor ingrese el origen de la Recta 2 --- tipo --- x,y --> 2,5 --> ")
	
	if m1==m2:
		return "Las rectas son paralelas y nunca se tocan"
		
	b1=(y1-(m1*x1))
	b2=(y2-(m2*x2))
	b2=float(b2)
	b1=float(b1)
	ptoX=((b2-b1)/(m1-m2))
	ptoY=(m1*ptoX)+b1

	return "\n""El punto de interseccion de las dos rectas es: ("+str(round(ptoX,2))+","+str(round(ptoY,2))+")"
	




print "\n""BIENVENIDO CALCULAX""\n"
print "1)""Definamos el maximo o minimo de una funcion cuadratica""\n"
print "2)""Ahora definamos las raices de un polinomio cuadratico""\n"
print "3)""Ahora calculamos el punto de interseccion entre dos rectas""\n"
dec=raw_input("Que desea hacer: ")
if dec=="1":
	print max_min()
if dec=="2":
	print raices()
elif dec=="3":
	print recta()
else:
	print "No entiendo su peticion..."
