#Tarea de Padilla. Version 1.0. 19/04/2020, domingo
#dado un fichero.txt con informacion, leerla, modificarla y mostrarla utilizando POO.
from io import open

listaNombres = open('D:\maykel\computacion\phyton\cOdIGoS\leyendo txt\lista_Padilla.txt','r')

leyendo = listaNombres.readlines()

listaNombres.close()

# hasta aqui leo el fichero lista_Padilla.txt donde tengo los datos
# este fichero esta en la misma carpeta que leyendo_listaPadilla.py
# pero puede darsele el camino que se desee

class Estudiante(): # creo la clase Estudiante con el constructor

	def __init__(self, nombre, edad,nota_quimica,nota_fisica,nota_matematica,nota_extra):
		self.nombre = nombre
		self.edad = edad
		self.nota_quimica = nota_quimica
		self.nota_fisica = nota_fisica
		self.nota_matematica = nota_matematica
		self.nota_extra = nota_extra

# la funcion siguiente,Estadistica_estudiante, retorna los valores en una **lista de diccionarios**,
# para poder manipularlos despues;como tal la representacion de estos datos puede ser como haga falta

	def Estadistica_estudiante(self):

		datos_lista = [{'nombre':self.nombre},{'edad':self.edad},{'nota_quimica':self.nota_quimica},
			{'nota_fisica':self.nota_fisica},{'nota_matematica':self.nota_matematica}]

		if self.nombre != 'Felipe':#si no es Felipe todos optamos como extra computacion jeje

			datos_lista.append({'nota_computacion':self.nota_extra})

		else:

			datos_lista.append({'nota_pajareria':self.nota_extra})# clase optativa de Felipe


		print(datos_lista) # imprimo lo anterior, esta es la salida de la funcion

# a continuacion,voy a iterar por la cantidad de filas de informacion que tengo en el texto
# si al txt le sumara mas informacion o restara, iteraria por la cantidad que exista...
# en este caso 5 veces

for fila in range(len(leyendo)):

	# a continuacion esta sintaxis es para poder extraer la informacion del txt
	#tuve que postear en stackoverflow para que me asistieran
	#https://es.stackoverflow.com/questions/347444/importar-txt-como-parametro-de-una-funcion?noredirect=1#comment627667_347444
	#porque no la podia obtener de la forma que me hacia falta
	#para podersela pasar como parametro a la instancia de la clase Estudiante,
	#en este caso estadisticas
	#aprendi algo nuevo: PARSING!!!

	nombre,edad,nota_quimica,nota_fisica,nota_matematica,nota_extra = leyendo[fila].split(',')

	#despues converti a numeros enteros las notas, se puede dejar string, PERO
	# cuando obtienes los datos de el txt, el ultimo valor sale por ejemplo '5\n',
	#esta molesta '\n' indica un salto de renglon y aparece en todos los ultimos valores de cada estudiante,
	#menos en el ultimo, porque no hay salto de renglon
	#cuando los paso a int desaparece ..

	edad = int(edad)

	nota_quimica = int(nota_quimica)

	nota_fisica = int(nota_fisica)

	nota_matematica = int(nota_matematica)

	nota_extra = int(nota_extra)

	#instancio la clase, o sea, creo el objeto estadisticas

	estadisticas = Estudiante(nombre, edad,nota_quimica,nota_fisica,nota_matematica,nota_extra)

	#nomenclatura del punto, nombre del objeto.metodo, y se ejecuta la funcion Estadistica_estudiante(),
	#que como estoy iterando me mostrara la informacion de todos lso estudiantes

	estadisticas.Estadistica_estudiante()


			
