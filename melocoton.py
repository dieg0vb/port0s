#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
__author__ = 'diego'
# Info:  NOTAS PYTHON, tabuleado y con limite direcho 80 Columnas
""" ########### CLASES Y METODOS ###############
"""


class NombreClase(object):
	"""
	Esto es una clase/prototipo/modelo/plantilla que realiza metodos/acciones/
	funciones con determinados comportamientos a partir de unos
	atributos/parametros. En vez de crearla con class nombreClase () "viejo estilo"
	se ha puesto "object" como referencia a una superclase ya que es el "nuevo
	estilo" que tre 3.x y que convive desde la 2.2 creo.
	"""

	def __init__(self, atributo1, atributoN):
		"""Metodo inicial
		Es similar al contructor el lenguajes estructurado, es opcional, se
        ejecuta tan pronto como un objeto es instanciado y defines los
        parametros que debes introducir al instaciar. self por lo general se
        refiere a la instancia cuyo método ha sido llamado, pero en __init__ se
        refiere al objeto recien creado. Por convención siempre será el primer
        argumento, pese a que al invocar un método no se especifique.
        (Python ya lo hace el solo)
        """
		# VariableGlobal = variableLocal
		self.atributo1 = atributo1
		self.atributoN = atributoN

	"""
    METODOS ESPECIALES
        __new__(cls, args)
Método exclusivo de las clases de nuevo estilo que se ejecuta antes que
__init__ y que se encarga de construir y devolver el objeto en sí. Equivalente
a los constructores de C++ o Java. Se trata de un método estático, es decir, que
existe con independencia de las instancias de la clase: es un método de clase,
no de objeto, y por lo tanto el primer parámetro no es self, sino la propia
clase: cls.

        __del__(self)
        Método llamado cuando el objeto va a ser borrado. También llamado destructor, se utiliza para realizar tareas de
        limpieza.

        __str__(self)
        Método llamado para crear una cadena de texto que represente a nuestro objeto. Se utiliza cuando usamos print
        para mostrar nuestro objeto o cuando usamos la función str(obj) para crear una cadena a partir de nuestro objeto

        __cmp__(self, otro)
        Método llamado cuando se utilizan los operadores de comparación para comprobar si nuestro objeto es menor, mayor
        o igual al objeto pasado como parámetro. Debe devolver un número negativo si nuestro objeto es menor, cero si
        son iguales, y un número positivo si nuestro objeto es mayor. Si este método no está definido y se intenta
        comparar el objeto mediante los operadores <, <=, > o >= se lanzará una excepción. Si se utilizan los
        operadores == o != para comprobar si dos objetos son iguales, se comprueba si son el mismo objeto
        (si tienen el mismo id).

        __len__(self)
        Método llamado para comprobar la longitud del objeto.
	"""

	# Métodos/Funciones que realiza la clase y el valor que retorna
	def metodo1(self):
		print "accion del método1 "
		resultadoMetodo1 = 1 + 1
		return resultadoMetodo1

	def metodoN(self):
		print "acción del método3"
		resultadoMetodoN = 1 + 1
		return resultadoMetodoN


"""
Crear objeto a partir de una clase se llama INSTANCIAR, para ello; asignamos a una variable el nombre
de la clase seguido sus respectivos parametros
"""
variableX = NombreClase(atributo1="atributoModificado",
						atributoN="atributoModificado")
"""
Si no definimos un método __init__ que hace estricto el paso de parametros jugamos con los parametros de las
funciones/metodos podemos hacer que sea variable el paso de parametros con el uso de *
"""


def funcionx(parametro1, parametro2, *parametroX):
	for j in parametroX:
		print j


funcionx(1, 2)
funcionx(1, 2, 3)
funcionx(1, 2, 3, 4)
"""
Esto funciona por que creamos una tupla de nombre parametroN en la que se almacena los parametros extra que los 2
iniciales por defecto. Si en vez de Tupla queremos un diccionario ponemos **. En este caso pasamos como parametro
el valor que contiene.
"""


def funcionx(parametro1, parametro2, **parametroX):
	for j in parametroX.items():
		print j


funcionx(1, 2)
funcionx(1, 2, tercero=3)
funcionx(1, 2, tercero=3, cuarto=4)
""" 
								Funciones de orden superior
ya que en python todo  son objetos, podemos pasar funciones como parametros a otras funciones y/o devolver funciones
como retorno"""


def saludar(idioma):
	def saludar_gal():
		print "Boas"

	def saludar_es():
		print "hola"

	def saludar_en():
		print "hi"

	idioma_funcion = {"gal": saludar_gal, "es": saludar_es, "en": saludar_en}
	return idioma_funcion[idioma]


llamada = saludar("gal")
llamada()
llamada = saludar("es")
llamada()
# Prdríamos acortar esto , los 1º parentesis indican los parametros de la funcion saludar y los segundos
# los de la funcion devuelta por saludar
saludar("gal")()
saludar("es")()

"""             ##############    HERENCIAS  ################
una nueva clase puede heredar todos los atributos y metodos de otra usada como plantilla
"""


class NuevaClase(NombreClase):
	pass  # Esto equivale a {} para definir clases vacias


# Herencia múltiple
class acuatico():
	pass


class terrestre():
	pass


class anfibio(acuatico, terrestre):
	pass


"""           ##################  POLIMORFISMO ################
Esto es usar operadores o funciones de diferentes formas. Prácticamente en clases significa que una clase
B heradada de A, no tiene que ser igual, puede ser modificada o diferente
"""


class Coche:
	"""Abstraccion de los objetos coche."""

	def __init__(self, gasolina):
		self.gasolina = gasolina
		print "Tenemos", gasolina, "litros"

	def arrancar(self):
		if self.gasolina > 0:
			print "Arranca"
		else:
			print "No arranca..."

	def conducir(self):
		if self.gasolina > 0:
			self.gasolina -= 1
			print "Quedan", self.gasolina, "litros"
		else:
			print "No se mueve..."


mi_coche = Coche(3)
print mi_coche.gasolina
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()
print mi_coche.gasolina

"""                  ################### ENCAPSULACION o privacidad #########################
Se refiere a impedir el aceso a determinados métodos o atributos desde fuera de las clases. Por defecto python no
lo impide y todos son publicos salvo que pongamos "__" delante de la variable o funcion que queremos limitar y python
solo las llama en determinadas condiciones y si no se dan python dará una excepción diciendo que no existe.
"""


class Clase():
	def metodoPubico(self):
		print "Esto es publico"

	def __metodoPrivado(self):
		print "Esto es privado"


x = Clase()
x.metodoPubico()
x.__metodoPrivado()
"""
Pero este psedo-proteccion se se basa en el renombrado interno de python, para ofuscarlas. Se puede saltar
con un truquito, llamandolas por su renombrado ya que se sabe que son "_nombreDeClase__nombreMetodo()"
"""
x._Clase__metodoPrivado()

"""                       ################# DICCIONARIOS ####################
Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una
clave y un valor. La clave es inmutable Esto es así porque los diccionarios se implementan como tablas hash, y a la
hora de introducir un nuevo par clave-valor en el diccionario se calcula el hash de la clave para después poder
encontrar la entrada correspondiente rápidamente.
"""
diccionario = {"Love Actually ": "Richard Curtis",
               "Kill Bill": "Tarantino",
               "Amélie": "Jean-Pierre Jeunet"
               }
"""
La diferencia principal entre los diccionarios y las listas o las tuplas es que a los valores almacenados en un
diccionario se les accede no por su índice, porque de hecho no tienen orden, sino por su clave, utilizando de
nuevo el operador [].
"""
diccionario["Love Actually"]  # devuelve "Richard Curtis"
diccionario["Kill Bill"] = "Quentin Tarantino"
"""
nombreDiccionario.get(k[, d])
Busca el valor de la clave k en el diccionario. Es equivalente a utilizar nombreDiccionario[k] pero al utilizar este
método podemos indicar un valor a devolver por defecto si no se encuentra la clave, mientras que con la sintaxis
nombrediccionario[k], de no existir la clave se lanzaría una excepción.

nombreDiccionario.has_key(k)
Comprueba si el diccionario tiene la clave k. Es equivalente a la sintaxis k in nombreDiccionario.

nombreDiccionario.items()
Devuelve una lista de tuplas con pares clave-valor.

nombreDiccionario.keys()
Devuelve una lista de las claves del diccionario.

nombreDiccionario.pop(k[, d])
Borra la clave k del diccionario y devuelve su valor. Si no se encuentra dicha clave se devuelve d si se especificó
el parámetro o bien se lanza una excepción.

nombreDiccionario.values()
Devuelve una lista de los valores del diccionario.
"""

"""                      ################ CADENAS ####################
nombreCadena.count(sub[, start[, end]])
Devuelve el número de veces que se encuentra sub en la cadena. Los parámetros opcionales start y end definen una
subcadena en la que buscar.

nombreCadena.find(sub[, start[, end]])
Devuelve la posición en la que se encontró por primera vez sub en la cadena o -1 si no se encontró.

nombreCadena.join(sequence)
Devuelve una cadena resultante de concatenar las cadenas de la secuencia seq separadas por nuestra cadena.

nombreCadena.partition(sep)
Busca el separador sep en la cadena y devuelve una tupla con la subcadena hasta dicho separador, el separador en
si, y la subcadena del separador hasta el final de la cadena. Si no se encuentra el separador, la tupla contendrá la
 cadena en si y dos cadenas vacías.

nombreCadena.replace(old, new[, count])
Devuelve una cadena en la que se han reemplazado todas las ocurrencias de la cadena old por la cadena new.
Si se especifica el parámetro count, este indica el número máximo de ocurrencias a reemplazar.

nombreCadena.split([sep [,maxsplit]])
Devuelve una lista conteniendo las subcadenas en las que se divide nuestra cadena al dividirlas por el
delimitador sep. En el caso de que no se especifique sep, se usan espacios. Si se especifica maxsplit, este indica
 el número máximo de particiones a realizar.
"""

"""                                ############# LISTAS ##################
La lista es un tipo de colección ordenada. Sería equivalente a lo que en otros lenguajes se conoce por arrays, o
vectores. Las listas pueden contener cualquier tipo de dato: números, cadenas, booleanos, … y también listas.
"""
lista = [22, True, "una lista", [1, 2]]
mi_var = lista[0]  # mi_var vale 22
mi_vari = lista[3][0]  # mi_var vale 1
lista[0] = 99  # l vale [99, True, "una lista", [1, 2]]
"""
Una curiosidad sobre el operador [] de Python es que podemos utilizar también números negativos. Si se utiliza un
número negativo como índice, esto se traduce en
que el índice empieza a contar desde el final, hacia la izquierda; es decir, con [-1] accederíamos al último elemento
de la lista, con [-2] al penúltimo, con [-3], al antepenúltimo, y así sucesivamente.
tambien permite el troceado con [inicio:fin:saltos0]
"""
mi_varia = lista[0:2]  # mi_var vale [99, True]
mi_variab = lista[0:4:2]  # mi_var vale [99, "una lista"]
"""
nombreLista.append(object)
Añade un objeto al final de la lista.

nombreLista.count(value)
Devuelve el número de veces que se encontró value en la lista.

nombreLista.extend(iterable)
Añade los elementos del iterable a la lista.

nombreLista.index(value[, start[, stop]])
Devuelve la posición en la que se encontró la primera ocurrencia de value. Si se especifican, start y stop definen
una sublista en la que buscar.

nombreLista.insert(index, object)
Inserta el objeto object en la posición index.

nombreLista.pop([index])
Devuelve el valor en la posición index y lo elimina de la lista. Si no se especifica la posición, se utiliza el
 último elemento de la lista.

nombreLista.remove(value)
Eliminar la primera ocurrencia de value en la lista.

nombreLista.reverse()
Invierte la lista. Esta función trabaja sobre la propia lista desde la que se invoca el método, no sobre una copia.

nombreLista.sort(cmp=None, key=None, reverse=False)
Ordena la lista. Si se especifica cmp, este debe ser una función que tome como parámetro dos valores x e y de la
lista y devuelva -1 si x es menor que y, 0 si son iguales y 1 si x es mayor que y.

El parámetro reverse es un booleano que indica si se debe ordenar la lista de forma inversa, lo que sería equivalente
a llamar primero a nombreLista.sort() y después a nombreLista.reverse().

Por último, si se especifica, el parámetro key debe ser una función que tome un elemento de la lista y devuelva una
clave a utilizar a la hora de comparar, en lugar del elemento en si.
"""

"""                         #################### TUPLAS #########################
Todolo que hemos explicado sobre las listas se aplica también a las tuplas, a excepción de la forma de definirla, en
la que se utiliza paréntesis en lugar de corchetes. En realidad el constructores es la "," y no el parentesis.
"""
tupla = (1, 2, True, "python")

"""                      ################### SENTENCIAS CONDICIONALES ###############
"""
pajaro = "loco"
if pajaro == "loco":
	print "pajaro " + pajaro
else:
	print "Solo un pajaro"

# Existen algunas formas contraidas:
numeroX = 3
numeroX = "par" if (numeroX % 2 == 0) else "impar"
print numeroX
"""
otra con contraccion "elif" que es un "else if", Ojo con el orden de las validaciones que aquí cabría esperar que
saliese "positivo mayor que 10" pero como se cumple antes "numeroX > 0" sale de la condición antes de lo esperado
"""
numeroX = 11
if numeroX < 0:
	print "Negativo"
elif numeroX > 0:
	print "Positivo"
elif numeroX > 10:
	print "Positivo mayor que 10"
else:
	print "Cero"

"""                     ######## BUCLES / CLICLOS ######
WHILE con "centinela" para romper ciclos infinitos
"""
while True:
	entrada = raw_input("Para salir excribe adios \n")
	if entrada == "adios":
		break
	else:
		print entrada

# otro forma con "centinela"
x = int(raw_input("Introduce un numero (* para terminar): "))
while x != "*":
	if x < 0:
		print "Numero negativo"
	elif x == 0:
		print "Has introducido el cero"
	else:
		print "El numero es positivo"
	x = int(raw_input("Introduce un numero (* para terminar): "))

"""                      FOR ... IN
Iteraciones sobre una secuencia. ("Para cada elemento en la secuencia...") ¿existe algo más cómodo/humano que esto?
"""
secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
	print elemento
# Tambien se puede usar "range"; para cada x in el rango de 1 a 10 con paso de 2, imprimelo (inicio, fin, paso)
for x in range(1, 10, 2):
	print x

"""                 Iteraciones con funciones construidas dentro de python
Permiten ahorrarnos los bucles típicos de otros lenguajes, con algo equivalente, con las funciones map, filter y reduce
"""
# map(funcion, secuencia[secuencia...])
# se pasa como parametros de la funcion, N secuencias y esta funcion debe aceptar las N secuencias
def cuadrado(numero):
	return numero ** 2


lista = [1, 2, 3, 4]
listaMapeada = map(cuadrado, lista)

# filter(funcion, secuencia)
# Verifica que los elementos de una secuencia cumplan una determinada condición, devolviendo TRUE o FALSE
def es_par(numero):
	return (numero % 2.0 == 0)


lista = [1, 2, 3, 4]
listaFiltrada = map(es_par, lista)

# reduce(funcion, secuencia)
# Aplica una funcion a pares de elementos de una secuencia hasta "reducirla" a un solo valor
def sumar(sumando1, sumando2):
	return sumando1 + sumando2


lista = [1, 2, 3, 4]
listaReducida = reduce(sumar, lista)
# listaReducida es (((1+2)+3)+4) = 10
