#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Resuelve el punto 7.6.6 del libro Algoritmos y programacion del capitulo 7 pagina 98
"""

def ordenar(lista, num):
	"""
	Dada una lista y un numeor genera 3 listas, donde ubica los mayores, menores e iguales al numero;
	PARAMETROS:
		Lista, Numero entero
	RETORNO:
		3 listas
	"""

	lista.sort()
	menores=[]
	mayores=[]
	iguales=[]
	multiplos=[]
	numero=lista.index(num)

	for pos in range(0,(numero)):
		menores.append(lista[pos])
	for pos in range((numero), (len(lista)-1)):
		if lista[pos]!=num:
			mayores.append(lista[pos])
	for pos in lista:
		if pos==num:
			iguales.append(pos)
	for pos in lista:
		if pos%num==0:
			multiplos.append(pos)


	if len(menores)==0:
		print "No hay numeros menores a "+str(numero)
	if len(mayores)==0:
		print "No hay numeros mayores a "+str(numero)
	if len(iguales)==0:
		print "No hay numeros iguales a "+str(numero)
	if len(multiplos)==0:
		print "No hay numeros multiplos de "+str(numero)
	

	return menores, mayores, iguales, multiplos


lista=[2,3,4,5,6,3,5,6,7,3,2,4,6,9,1,0,8]
numero=int(input("Ingrese el numero: "))

print ordenar(lista, numero)