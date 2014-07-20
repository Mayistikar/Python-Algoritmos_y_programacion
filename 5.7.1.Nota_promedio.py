#!/usr/bin/env python 
#-*-coding:utf-8-*-

"""
Este soft pide una a una las notas del usuario y saca el promedio de ellas;
responde el punto 5.7.1 del libro Algoritmos y Programacion capitulo 4 pagina 65
"""

def nota_promedio():
	confir="n"
	contador=0.0
	nota=0
	while confir=="N" or confir=="n":
		contador+=1
		nota+=input("Ingrese su nota: ")
		confir=raw_input("son todas las notas? s/n: ")
	return nota/contador

print nota_promedio()

