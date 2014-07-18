#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este programa determina el signo zodiacal de una persona desde su fecha de nacimiento;
con el se resuelve el punto 4.6.8 del libro Algoritmos y Programacion capitulo 4 en pagina 55
"""


"""	
Aries: 21 de marzo al 20 de abril.
Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 21 de junio.
Cancer: 22 de junio al 23 de julio.
Leo: 24 de julio al 23 de agosto.
Virgo: 24 de agosto al 23 de septiembre.
Libra: 24 de septiembre al 22 de octubre.
Escorpio: 23 de octubre al 22 de noviembre.
Sagitario: 23 de noviembre al 21 de diciembre.
Capricornio: 22 de diciembre al 20 de enero.
Acuario: 21 de enero al 19 de febrero.
Piscis: 20 de febrero al 20 de marzo.
"""

def zodiacal(d,m):
	if (d>=21 and m==3)or(d<=20 and m==4):
		return "Su signo es Aries!"
	if (d>=21 and m==4)or(d<=20 and m==5):
		return "Su signo es Tauro!"
	if (d>=21 and m==5)or(d<=20 and m==6):
		return "Su signo es Geminis!"
	if (d>=21 and m==6)or(d<=20 and m==7):
		return "Su signo es Cancer!"
	if (d>=21 and m==7)or(d<=20 and m==8):
		return "Su signo es Leo!"
	if (d>=21 and m==8)or(d<=20 and m==9):
		return "Su signo es Virgo!"
	if (d>=21 and m==9)or(d<=20 and m==10):
		return "Su signo es Libra!"
	if (d>=21 and m==10)or(d<=20 and m==11):
		return "Su signo es Escorpio!"
	if (d>=21 and m==11)or(d<=20 and m==12):
		return "Su signo es Sagitario!"
	if (d>=21 and m==12)or(d<=20 and m==1):
		return "Su signo es Capricornio!"
	if (d>=21 and m==1)or(d<=20 and m==2):
		return "Su signo es Acuario!"
	if (d>=21 and m==2)or(d<=20 and m==3):
		return "Su signo es Piscis!"

print "LE DIREMOS SU SIGNO ZODIACAL"
print " 1) Enero ", " 2) Febrero ", " 3) Marzo ", " 4) Abril ", " 5) Mayo ""\n", " 6) Junio ", " 7) Julio ", " 8) Agosto ", " 9) Septiembre ", " 10) Octubre ""\n", " 11) Noviembre ", " 12) Diciembre""\n"
m=input("El numero del mes en que nacio: ")

if m>=1 or m<=12:
	print "Dato ingresado...""\n"
	d=input("Ingrese el dia en que nacio: ")
	if d>28 and m==2:
		print "Ese dia no existe ... febrero tiene 28 dias..."
	elif d>30 and (m==4 or m==6 or m==9 or m==11 or d<0):
		print "Ese dia no existe..."
	elif d>31 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
		print "Ese dia no existe..."
	else:
		print zodiacal(d,m)
else:
	print "No existe dicho mes..."
