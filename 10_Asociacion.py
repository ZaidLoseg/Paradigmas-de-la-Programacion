#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#================================

#=====================================
# La clase A tiene tres numeros reales
#=====================================
class A:
	__a:float=0.0
	__b:float=0.0
	__c:float=0.0

	def __init__(mi,a:float,b:float,c:float):
		mi.a = a
		mi.b = b
		mi.c = c

#===================================
# La clase B tiene numeros reales
#===================================
class B:
	__d:float = 0.0
	__e:float = 0.0
	def __init__(mi,d:float,e:float):
		mi.d = d
		mi.e = e

	#=======================================
	#Metodo sumar todo (internos + extremos)
	#=======================================
	def sumar_todo(mi,aa:float, bb:float):
		x:float=mi.d+mi.e+aa+bb
		return x
#=============================
# ASOCIACION
# USANDO OBJETOS INDEPENDIENTES
#=============================
objetoA = A(1.0,2.0,3.0)
objetoB= B(4.0,5.0)
print(objetoB.sumar_todo(objetoA.a,objetoA.b))

#======================================
# El objeto c tiene dos reales y un objeto A
# El objeto A se intancia dentro de C
#======================================
class C:
	__d:float=0.0
	__e:float=0.0
	__Aa:A = None

	def __init__(mi,d:float,e:float):
		mi.d = d
		mi.e = e
		# A esta instanciado adentro
		mi.Aa = A(1.0,2.0,3.0)

	def sumar_todo(mi):
		x:float = mi.d+mi.e+mi.Aa.a+mi.Aa.b)
		return x

#================================
# Composicion
# Contiene otro objeto dentro
#================================
objetoC = C(4.0,5.0)
print(objetoC.sumar_todo())

#========================================
# Objeto D tiene dos reales y un objeto A
# definido por fuera
#========================================
class D:
	__d:float = 0.0
	__e:float = 0.0
	_Aa: A = None
	
	def __init__(mi,d:float,e:float,Aa:A):
		mi.d = d
		mi.e = e
		mi.Aa = Aa
	
	def sumar_todo(mi):
		x:float=mi.d+mi.e+mi.Aa.a+mi.Aa.b
		return x

#=========================================
# AGREGACION
# Contrusye el objeto agregado por fuera
#=========================================
objetoD = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())













