#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#=================================

#=================================
# PROGRAMACION ORIENTADA A OBJETOS
#=================================

#=================================
# Una clase para un objeto vacio
# No esta tan vacio, necesita
# la palabra pass = pasar
#=================================

class ObjetoVacio:
  pass


#===============================================
# Nada es la instancion de la clase ObjetoVacio
#===============================================
nada = ObjetoVacio()
print(type(nada))

#=================
# La clase llanta
#=================
class llanta:
	#=================================
	# variable cuenta es toda la clase
	#=================================
	cuenta = 0
	#========================================
	# Funcion constructora de identidad
	# __init__ es una funcion reservada
	# comienza con uno mismo: self
	# pero puede ser otro nombre (mi)
	# parametro de entrada default
	#=========================================
	def __init__(mi,radio=50,ancho=30,presion=1.5):
		# variable de la estructura completa llanta
		llanta.cuenta += 1
		# variables exclusivas de cada objeto
		mi.radio = radio
		mi.ancho = ancho
		mi.presion = presion

#==========================
# Objetos (instanciados)
#==========================

llanta1 = llanta(50,30,1.5)
llanta2 = llanta(presion = 1.2)
llanta3 = llanta()
llanta4 = llanta(40,30,1.6)

#======================================
# Objetos que contienen otros objetos
#======================================
class Coche:
	def __init__(mi,ll1,ll2,ll3,ll4):
		mi.llanta1 = ll1
		mi.llanta2 = ll2
		mi.llanta3 = ll3
		mi.llanta4 = ll4
micoche= Coche(llanta1,llanta2,llanta3,llanta4)

print("Total de llantas ",llanta.cuenta) 
print("presion de la llanta 4 = ",llanta4.presion)
print("radio de la llanta 4 = ",llanta4.radio)
print("radio de la llanta 3 = ",llanta3.radio)
print("presion de la llanta 1 de mi choche = ",micoche.llanta1.presion)

#======================
# Encapsulamiento
#======================

#=====================================================================
# Uso de la funcion de python propery para poner y obtener atributos
# a variables protegidas con __
#=====================================================================
class estudiante:
	def __init__(mi):
		mi.__nombre = ''
	def ponerme_nombre(mi,nombre):
		print("se llamo a ponerme_nombre")
		mi.nombre = nombre
	def obtener_nombre(mi):
		print("se llamo a obtener nombre")
		return mi.nombre
	nombre=property(obtener_nombre,ponerme_nombre)

#===================================
# crear objeto estudiante sin nombre
#===================================
estudiante = estudiante()

#========================================================================
# Ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre
# (sin tener que llamar explicitamente la funcion)
#========================================================================
estudiante.nombre = "Diego"

#=========================================================================
# Obtener el nombre con el metodo obtener nombre
# __nombre es una variable encapsulada  ( no visible desde fuera)
# (sin tener que llamar explicitamente a la funcion obtener_nombre)
#==========================================================================
print(estudiante.nombre)

# Esto no funciona 
# print(estudiante.__nombre

#==========================
# Herencia de clases
#==========================
class Cuadrilatero:
	def __init__(mi,a,b,c,d):
		mi.lado1=a
		mi.lado2=b
		mi.lado3=c
		mi.lado4=d

	def perimetro(mi):
		p=mi.lado1+mi.lado2+mi.lado3+mi.lado4
		print("perimetro = ",p)
		return p

#====================================
# Su hijo rectangulo
# Rectangulo es hijo de cuadrilatero
# Rectangulo(Cuadrilatero)
#====================================
class Rectangulo(Cuadrilatero):
	def __init__(mi,a,b):
		#==========================
		# Constructor de su madre
		#==========================
		super().__init__(a,b,a,b)

#=============================
# Su nieto cuadrado
# Hijo de rectangulo
#=============================
class cuadrado(Rectangulo):
	def __init__(mi,a):
		super().__init__(a,a)
	def area(mi):
		area = mi.lado1**2
		return area

	#def perimetro(mi):
	#	p=4.0*mi.lado1
	#	print("perimetro =",p)
	#	return p

#========================
# crear un cuadrado
#========================
cuadrado1= cuadrado(5)

#=====================================================
# llamar al metodo perimetro de su abuelo cuadrilatero
#=====================================================

perimetro1 = cuadrado1.perimetro()

#====================================
# llamar a su propio metodo area
#====================================
area1 = cuadrado1.area()

print("perimetro = ", perimetro1)
print("Area = ", area1)

#==================================================================
# Sobre-escribir un metodo de su madre o abuela o tatarabuela....
# Es volver a definir una funcion ya existente
#==================================================================

