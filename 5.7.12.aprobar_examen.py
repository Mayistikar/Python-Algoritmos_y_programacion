#!/usr/bin/env python
#-*-conding:utf-8-*-


"""
Este codigo muestra si un alumno aprobo o no un examen en base a los puntos resueltos;
Resuelve el punto 5.7.12 del libro Algoritmos y Programacion\capitulo 5\pagina 66
"""

def aprobar():
	pts_exam=3
	while pts_exam!= 999:
		pts_exam=int (input("Ingrese el total de puntos del examen(Ingrese 999 para salir): "))
		pts_aprob=int (input("Ingrese el numero de ptos aprobados: "))
		porcentaje=(pts_aprob*100)/pts_exam
		if porcentaje>=60:
			print ("\n""Aprueba el examen con un puntaje de "+str(porcentaje)+"\n")
		else:
			print ("Ah reprobado el examen...")

	return

aprobar()






