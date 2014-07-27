#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Este codigo permite inscribir a los usuarios en una lista;
Resuelve el punto 7.6-7-8 del libro Algoritmos y programacion del capitulo 7 pagina 93
"""


def borrar(usuario, inscritos):
	"""
	Esta funcion toma una lista y un elemento de la lista y lo borra si existe
	PARAMETROS:
		Un elemento entero  y una lista
	RETORNO:
		Una lista con el usuario borrado
	"""

	if usuario not in inscritos:
		print "Usted no se encuentra en lista"
	else:
		inscritos.remove(usuario)
	return inscritos

def agregar(usuario, inscritos):

	"""
	Esta funcion toma una lista y un elemento de la lista y lo agreaga solo si es un entero positivo
	PARAMETROS:
		Un elemento entero  y una lista
	RETORNO:
		Una lista con el usuario agregado
	"""

	while usuario>0:
		if usuario not in inscritos:
			inscritos.append(usuario)
		else:
			print "Este ID ya esta inscrito..."
		usuario=int(input("Inscriba su ID en lista(0 para terminar): "))

	return inscritos

inscritos=[1234]

#-------------------------MENU---------------------------------

print "\n""BIENVENID@""\n"
print "1)""Agregar su nombre a la lista""\n"
print "2)""Borrar su nombre de la lista""\n"
dec=raw_input("Que desea hacer: ")

if dec=="1":
	usuario=raw_input("Inscriba su ID en lista junto con el nombre y apellido: ")
	print agregar(usuario, inscritos)
elif dec=="2":
	usuario=raw_input("Inscriba su ID en lista junto con el nombre y apellido: ")
	print borrar(usuario, inscritos)
else:
	print "No entiendo su peticion..."



