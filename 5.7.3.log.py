#!/usr/bin/env python
#-*-coding-utf-8-*-

"""
Este programa hace el logueo... con contrasenas... las verifica y responde;
Resuelve el punto 5.7.3 del libro Algoritmos y Programacion capitulo 5 pagina 65
"""
import time

def loguear1():
	password=0000
	while password!="hack":
		password=raw_input("Ingrese su contrasena: ")
	print "Bienvenido!!!"
	return

def loguear2():
	intentos=0
	while intentos!=11:
		intentos+=1
		password=raw_input("Ingrese su contrasena: ")
		if password=="hack":
			print "Bienvenido!!!"
			break
		elif intentos==10:
			print "lo siento demasiados intentos"	
			break
		else:
			print "Contrasena erronea... Intente nuevamente...""\n"
	
	return

def loguear3():
	t=0
	password="00000"
	while password!="hack":
		password=raw_input("Ingrese su contrasena: ")
		if password=="hack":
			print "Bienvenido!!!"
			break
		else:
			print "Contrasena erronea... Intente nuevamente...""\n"
		time.sleep(t)
		t+=2

def loguear4():
	password="00000"
	while password!="hack":
		password=raw_input("Ingrese su contrasena: ")
		if password=="hack":
			return True

		else:
			return False

	
print loguear4()
loguear3()		
loguear1()
loguear2()