#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este programa recibe el numero de un dia del ano entre 1 y 365 y dice que dia es;
Se resuelve el ejercicio 4.6.6 del libro Algoritmos y Programacion del capitulo 4 pagina 55
"""

def que_dia():
	num=input("Ingrese el numero del dia: ")
	r=num%7
	if r==1:
		return "Es lunes"
	if r==2:
		return "Es Martes"
	if r==3:
		return "Es Miercoles"
	if r==4:
		return "Es Jueves"
	if r==5:
		return "Es Viernes"
	if r==6:
		return "Es Sabado"
	if r==0:
		return "Es Domingo"

print que_dia()