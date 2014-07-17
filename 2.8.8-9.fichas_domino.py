#!/usr/bin/env python
#-*-coding:utf-8-*-

"""Genera fichas de domino con numeros en vez de pts"""

def genera(rang):
	for x in range(rang+1):
		print "\n""*********""\n"
		for z in range(rang+1):
			print " __ "
			print "|"+str(x)+" |"
			print " -- "
			print "|"+str(z)+" |"
			print " -- "
		print "\n""*********""\n"
		
	return

def rango():
	rang=input("Determine el numero maximo en ficha: ")
	genera(rang)


rango()