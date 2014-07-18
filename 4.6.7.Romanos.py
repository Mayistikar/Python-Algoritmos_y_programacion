#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este programa cambia un numero entre (1 y 3999)escrito en  numeros arabigos y lo traduce a romanos;
Con el desarrollo el punto 4.6.7  del libro Algoritmos y Programacion capitulo 4 pagina 55
"""

z1="I"
z5="V"
z10="X"
z50="L"

romano=[]
def romanos():
	z=input("Ingrese el numero arabigo: ")
	zs=z/1000
	cent=z%1000
	cents=cent//100
	dece=cent%100
	deces=dece//10
	unid=dece%10
	rom="Romano "

	if z<4000:
		for div in range (zs):		#Trabaja con las unidades de mil del numero
			rom+="M"

		if cents>=0 and cents<=3:		#Trabaja con las centenas del numero
			for div in range(cents):
				rom+="C"
		elif cents==4:
			rom+="CD"
		elif cents==5:
			rom+="D"
		elif cents>=6 and cents<=8:
			rom+="D"
			for div in range(5,cents):
				rom+="C"
		else:
			rom+="CM"
			

		if deces>=0 and deces<=3:		#Trabaja con las deceenas del numero
			for div in range(deces):
				rom+="X"
		elif deces==4:
			rom+="XL"
		elif deces==5:
			rom+="L"
		elif deces>=6 and deces<=8:
			rom+="L"
			for div in range(5,deces):
				rom+="X"
		else:
			rom+="XC"

		if unid>=0 and unid<=3:		#Trabaja con las unidades del numero
			for div in range(unid):
				rom+="I"
		elif unid==4:
			rom+="IV"
		elif unid==5:
			rom+="V"
		elif unid>=6 and unid<=8:
			rom+="V"
			for div in range(5,unid):
				rom+="I"
		else:
			rom+="IX"
	return rom
print romanos()