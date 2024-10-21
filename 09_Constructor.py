#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#=================================

#================================
# Clase  computadora
#================================

class computadora:
	marca: str = None
	capacidad: int = 0
	ram: int = 0

	#=======================
	# Constructor
	#=======================
	def __init__(mi,marca:str, capacidad:int,ram:int):
		print(f"Accediendo al constructor de la pc: {marca}")
		mi.marca = marca
		mi.capacidad = capacidad
		mi.ram = ram

	def imprimirInfoPC(mi):
		print(f"Esta es la computadora marca: {mi.marca} con almacenamiento de {mi.capacidad}GB y memoria de {mi.ram}GB

	#=====================
	# Destructor
	#=====================
	def __del__(mi):
		print(f"Se elimino de la computadora: {mi.marca}


#========================
# Clase persona
#========================
class Persona:
	nombres: str = None
	apellido: str = None
	edad int = 0
	direccion: str = None
	computadora: computadora = none
	
	#===============================
	# Constructor de persona
	#===============================
	def __init__(mi,nombres:str,apellido:str,edad:int, direccion:str, marca:str, capacidad:int, ram:int):
		mi.nombres = nombres
		mi.apellidos = apellidos
		mi.edad = edad
		mi.direccion = direccion
		mi.computadora = computadora(marca,capacidad,ram)
		print(f"---Accedimos al constructor de la persona: {nombres} {apellidos}")

	def imprimirinfo(mi) -> None:
		print(f"---Mi nombre es {mi.nombre} {mi.apellidos, tengo {mi.edad} años de edad, y vivo en {mi.direccion}")
		mi.computadora.imprimirinfo()

	#==================
	# Destructor
	#==================
	def __del__(mi):
		print(f"--Eliminamos a la persona...{mi.nombre} {mi.apellidos})

#==================================
# Funcion 1 es el programa
#==================================
def funcion1():
	persona1 = persona("Carlos","Perez",40,"Xochimilco","Lenovo",700,8)
	print("\n")
	persona.imprimirinfo()
	print("\n")
	persona2 = persona("Magdalena","Carrillo",35,"Jalapa","IBM",200,4)
	print("\n")
	persona2.imprimirinfo()
	print("\n")

funcion1()

