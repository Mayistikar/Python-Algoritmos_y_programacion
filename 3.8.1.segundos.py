#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""Este programa resuelve el punto 3.8.1 del libro Algoritmos y Programacion"""

def seg(h,m,s):
	"""Implementa la cantidad de segundos en un tiempo determinado, 
	ingresado como horas,minutos,segundos"""
	print "En "+str(h)+":"+str(m)+":"+str(s)+" hay: "+str((h*3600)+(m*60)+s)+" segundos."
	h*=3600
	m*=60
	return h+m+s


def tiempo(s):
	"""Implementa un tiempo ingresado en segundos y retorna la cantidad
	expuesta en horas, minuts y segundos"""

	if s/3600>0:
		h=s/3600
		m=(s%3600)/60
		s1=(s%3600)%60
		return "Hay "+str(h)+" horas con "+str(m)+" minutos con "+str(s1)+" segundos."

def dos_tiempos():
	print "Ingrese el tiempo uno con este formato (horas,minutos,segundos): "
	h1=input ("cuantas horas: ")
	m1=input ("cuantos minutos: ")
	s1=input ("cuantos segundos: ")
	print "\n""Ingrse el tiempo dos con este formato (horas,minutos,segundos): "
	h2=input ("cuantas horas: ")
	m2=input ("cuantos minutos: ")
	s2=input ("cuantos segundos: ")
	seg1=seg(h1,m1,s1)
	seg2=seg(h2,m2,s2)
	return "La cantidad total es: "+tiempo((seg1+seg2))


"-----------------------MENU PRINCIPAL------------------------"

print "BIENVENID@ A SU CONVERSOR DE TIEMPOS"		
print "(1)"+"Conversion a segundos desde un tiempo en h/m/s"
print "(2)"+"Conversion a h/m/s desde un tiempo en segundos"
print "(3)"+"Dados dos tiempos encontrar la suma y expresarlos en h/m/s"
z=raw_input("Porfavor ingrese su opcion: ")
if z=="1":
	print "Ingresa el tiempo en formato(h/m/s)"
	hx=input("Cuantas horas: ")
	mx=input("cuantos minutos: ")
	sx=input("cuantos segundos: ")
	seg(hx,mx,sx)	
elif z=="2":
	print "Ingresa el tiempo en segundos"
	st=input("Cuantos segundos: ")
	print tiempo(st)
elif z=="3":
	print dos_tiempos()



