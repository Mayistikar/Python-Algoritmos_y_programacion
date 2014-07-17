#!/usr/bin/env python
#-*-coding:utf-8;-*-

"""Este sof permite escribir una palabra mil veces"""

def milpalabra():
	palabra=raw_input("Escribe la palabra: ")
	for x in range(1,1001):
		print str(x)+" "+palabra

milpalabra()
