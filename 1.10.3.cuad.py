#!/usr/bin/env python
#-*-coding:utf-8;-*-
"""este programa pone un numero al lado de su cuadrado"""

def nom_cuad():
	n1=input("Escriba el primer numero: ")
	n2=input("Escriba el segundo numero: ")
	for ns in range(n1,n2):
		print ns, ns**2
	return

nom_cuad()