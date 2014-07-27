#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Un menu sencillo reutilizable y util
"""



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
