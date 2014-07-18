#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este programa resuelve los distintas peticiones descritas en cada funcion;
es el resultado de resolver el punto 4.5.6 del libro Algoritmos y Programacion capitulo 4 pag 55
"""

def biciesto():
	"""
	Esta funcion determina si un ano es biciesto... y returna un string si / no
	"""
	ano=input("Ingresar el ano a revisar: ")
	if ano%4==0 and ano%100!=0:
		return "Es biciesto!"
	elif ano%4==0 and ano%100!=0 and ano%400==0:
		return "\n""Es biciesto!"
	else:
		return "\n""No es biciesto!"

def dias_mes(m):
	"""
	Dado un mes retorna la cantidad de dias que tiene
	PARAMETRO:
		numero del mes... impreso en el menu
	RETORNA:
		El numero de dias en un entero
	"""
	m=str(m)
	if m=="4" or m=="6" or m=="9" or m=="11":
		return 30
	elif m=="2":
		return 28
	elif m=="1" or m=="3" or m=="5" or m=="7" or m=="8" or m=="10" or m=="12":
		return 31
	else:
		print  "\n""Este mes NO EXISTE!"
		return 

def fin_mes(d,m):
	"""
	Esta funcion determina cuantos dias faltan para fin de mes
	PARAMETRO:
		Necesita dias ingresados como un entero y el mes
	RETORNA:
		Un entero que son los dias faltantes
	"""
	print "\n""Faltan "+str(dias_mes(m)-d)+" Para que se acabe el mes :)"
	return

def validacion():
	"""
	Esta funcion valida una fecha... se ingresa con el formato (dia,mes,ano)
	"""
	(d,m,a)=input ("Porfavor ingresa la fecha con formato (d/m/a) de esta manera (13,10,1982)... ")

	if d>dias_mes(str(m)):
		return "\n""La fecha no existe..."
	elif a<0:
		return "\n""La fecha no existe..."
	elif m>12 or m<=0:
		return "\n""La fecha no existe..."
	else:
		return "\n""Es una fecha valida :)"

def fin_ano(d,m):
	"""
	Esta funcion permite calcular la cantidad de dias que faltan para completar el ano
	PARAMETRO:
		Requiere el dia y el mes como parametro en un entero
	RETORNA:
		El numero de dias que faltan para terminar el ano
	"""
	m=int(m)
	total=0
	for mes in range (1,m):
		total+=dias_mes(mes)

	total=(365-d)-total
	return total

def entre_fechas(d1,m1,a1,d2,m2,a2):
	"""
	Esta funcion permite calcular la cantidad de dias que hay entre dos fechas
	PARAMETRO:
		Requiere 6 parametros en formato entero referentes a los datos de las fechas
		el formato es dia1, mes1, ano1, dia2, mes2, ano2
	RETORNA:
		El numero de dias que hay entre los anos
	"""
	tano=a2-a1
	diax1=fin_ano(d1,m1)
	diax2=365-fin_ano(d2,m2)
	totaldias=0
	if tano==1:
		totaldias=diax1+diax2
	elif tano==0:
		totaldias=fin_ano(d1,m1)-fin_ano(d2,m2)
	else:
		totaldias=diax1+diax2+(365*tano)

	anos=(totaldias/365)-1
	meses=(totaldias%365)/30
	diasrest=((totaldias%365)%30)

	print "Han pasado "+str(anos)+" anos con "+str(meses)+" meses con "+str(diasrest)+" dias!!!"

"---------------------MENU----------------------"

print "\n""BIENVENIDO CALENDARIO""\n"
print "1)""Quieres saber si un ano es biciesto?""\n"
print "2)""Quieres saber cuantos dias tiene un mes?""\n"
print "3)""Quieres saber si una fecha es valida?""\n"
print "4)""Quieres saber cuantos dias faltan para terminar el mes?""\n"
print "5)""Quieres saber cuantos dias faltan para terminar el ano?""\n"
print "6)""Quieres saber cuantos dias hay entre dos fechas?""\n"
dec=raw_input("Que desea hacer: ")
print 


if dec=="1":
	print biciesto()

elif dec=="2":
	print " 1) Enero ", " 2) Febrero ", " 3) Marzo ", " 4) Abril ", " 5) Mayo ""\n", " 6) Junio ", " 7) Julio ", " 8) Agosto ", " 9) Septiembre ", " 10) Octubre ""\n", " 11) Noviembre ", " 12) Diciembre""\n"
	mes=raw_input("Escoge tu mes: ")
	dix=dias_mes(mes)
	if dix == 28:
		print "\n""Este mes tiene 28 dias!""\n"
	elif dix == 30:
		print "\n""Este mes tiene 30 dias!""\n"
	elif dix == 31:
		print "\n""Este mes tiene 31 dias!""\n"

elif dec=="3":
	print validacion()

elif dec=="4":
	dia=input("El numero del dia: ")
	print " 1) Enero ", " 2) Febrero ", " 3) Marzo ", " 4) Abril ", " 5) Mayo ""\n", " 6) Junio ", " 7) Julio ", " 8) Agosto ", " 9) Septiembre ", " 10) Octubre ""\n", " 11) Noviembre ", " 12) Diciembre""\n"
	mes=raw_input("El numero del mes: ")
	fin_mes(dia,mes)

elif dec=="5":
	di=input("El numero del dia: ")
	print " 1) Enero ", " 2) Febrero ", " 3) Marzo ", " 4) Abril ", " 5) Mayo ""\n", " 6) Junio ", " 7) Julio ", " 8) Agosto ", " 9) Septiembre ", " 10) Octubre ""\n", " 11) Noviembre ", " 12) Diciembre""\n"
	me=input("El numero del mes: ")
	dias1=fin_ano(di,me)
	print "\n""Quedan "+str(dias1)+" para terminar el ano!""\n"
	print "Han transcurridos "+str((365-dias1))+" dias hasta la fecha!"

elif dec=="6":
	print "Defina la primera fecha (debe ser anterior a la segunda!!!): ""\n"
	d1=input("El numero del dia: ")
	print " 1) Enero ", " 2) Febrero ", " 3) Marzo ", " 4) Abril ", " 5) Mayo ""\n", " 6) Junio ", " 7) Julio ", " 8) Agosto ", " 9) Septiembre ", " 10) Octubre ""\n", " 11) Noviembre ", " 12) Diciembre""\n"
	m1=raw_input("El numero del mes: ")
	a1=input("El ano: ")
	print "\n""Defina la segunda fecha ""\n"
	d2=input("El numero del dia: ")
	print " 1) Enero ", " 2) Febrero ", " 3) Marzo ", " 4) Abril ", " 5) Mayo ""\n", " 6) Junio ", " 7) Julio ", " 8) Agosto ", " 9) Septiembre ", " 10) Octubre ""\n", " 11) Noviembre ", " 12) Diciembre""\n"
	m2=raw_input("El numero del mes: ")
	a2=input("El ano: ")
	print entre_fechas(d1,m1,a1,d2,m2,a2)

else:
	print "No entiendo su peticion..."
