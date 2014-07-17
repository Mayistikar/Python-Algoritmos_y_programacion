#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""este programa resuelve en su totalidad los cilos del ejercicio 2.8.1 del libro 
algoritmos y programacion pag 33"""


def ciclo1():#imprime los numeros del 10 al 20
	for x in range(10,21):
		print x
	return

def fivefriends():	#imprime un saludo a tus cinco mejores amigos
	f1=raw_input("Escribe el nombre de tu mejor primer amigo:")
	f2=raw_input("Escribe el nombre de tu mejor segundo amigo:")
	f3=raw_input("Escribe el nombre de tu mejor tercer amigo:")
	f4=raw_input("Escribe el nombre de tu mejor cuarto amigo:")
	f5=raw_input("Escribe el nombre de tu mejor quinto amigo:")
	print "Un saludo enorme para... "+f1+" y "+f2+" y "+f3+" y "+f4+" y "+f5
	return 


def enemigos(): #En esta funcion resuelvo los ejercicios 5 y 6 por que son similares
#imprime un saludo a los enemigos que ingrese el usuario.
	saludo="Que se jodan... "
	for enemigo in range(6):
		enemis=raw_input("Escribe el nombre de tu enemigo  ")
		saludo+=enemis+" "
	print saludo 
	return

def cuantos():
	cant=input("A cuantos amigos quieres saludar: ")
	amig=raw_input("Ingresa el nombre de un amigo  ")
	for x in range(1,cant):
		ask=raw_input("escribe el nombre de otro amigo ")
		amig+=" y "+ask
	print "Un saludo para "+amig
	return

print "\n""BIENVENID@ AL CICLO DE SALUDOS"'\n'
print "Escoge una opcion""\n"
print "(1) Imprimir los numeros del 10 al 20"
print "(2) Saludar a tus 5 mejores amigos"
print "(3) Enviar un saludo a 5 enemigos"
print "(4) Escojer cuantos amigos saludar y enviale el saludo""\n"
var=raw_input("Escoge una opcion ")

if var=="1":
	ciclo1()
elif var=="2":
	fivefriends() 
elif var=="3":
	enemigos() 
elif var=="4":
	cuantos() 
else:
	print "No entiendo tu peticion "


		