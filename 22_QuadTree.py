
#====================================
#  Zaid Lopez Segura
#====================================
# Matematica Algoritmica
# ESFM IPN
# Septiembre 2024
#====================================

#=================================
# Paquetes externos
#=================================
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#==========================
# Particula x,y
#==========================

class Particula():
	def __init__(mi,x:float, y:float):
		mi.x = x
		mi.y = y

#=======================================================================
# Cajas para las particulas definidas por la esquina inferior izquierda
# (x0,y0): esquina (w,h) alto y ancho de la caja
#=======================================================================

class Nodo():
	def __init__(mi,x0:float,y0:float, w:float,h:float, particulas):
		mi.x0 = x0
		mi.y0 = y0
		mi.ancho = w
		mi.alto = h
		mi.particulas = particulas
		mi.hijos = []

	def get_ancho(mi):
		return mi.ancho
	
	def get_alto(mi):
		return mi.alto
	
	def get_particulas(mi):
		return mi.particulas

#=======================================================
# Funcion subdivision de cajas (en cuatro hijos)
# se llama a si misma para seguir dividiendo 
# a las siguientes generaciones
#========================================================

def subdivision_recursiva(nodo:Nodo, k:int):
	if len(nodo.particulas)<=k:
		return

	w_ = float(0.5*nodo.ancho)
	h_ = float(0.5*nodo.alto)

	p = cuantas_contiene(nodo.x0, nodo.y0, w_,h_, nodo.particulas)
	nodo.x1 = Nodo(nodo.x0, nodo.y0, w_, h_, p)
	subdivision_recursiva(nodo.x1,k)

	p = cuantas_contiene(nodo.x0, nodo.y0+h_, w_, h_, nodo.particulas)
	nodo.x2 = Nodo(nodo.x0, nodo.y0+h_, w_, h_,p)
	subdivision_recursiva(nodo.x2,k)


	p = cuantas_contiene(nodo.x0+w_, nodo.y0, w_, h_, nodo.particulas)
	nodo.x3 = Nodo(nodo.x0+w_, nodo.y0, w_, h_, p)
	subdivision_recursiva(nodo.x3,k)

	p = cuantas_contiene(nodo.x0+w_, nodo.y0+h_, w_, h_, nodo.particulas)
	nodo.x4 = Nodo(nodo.x0+w_, nodo.y0+h_, w_, h_, p)
	subdivision_recursiva(nodo.x4,k)

	nodo.hijos = [nodo.x1, nodo.x2, nodo.x3, nodo.x4]

#=============================================
# Funcion para incluir particulas en una caja
#=============================================
def cuantas_contiene(x:float,y:float,w:float,h:float,particulas):
	pts=[]
	for particula in particulas:
		if particula.x >= x and particula.x <= x+w and particula.y >= y and particula.y <=y+h:
			pts.append(particula)
	return pts

#=====================================
# Funcion para encontrar cajas hijas
#=====================================
def encontrar_hijos(nodo):
	if not nodo.hijos:
		return [nodo]
	else:
		hijos = []
		for hijo in nodo.hijos:
			hijos += (encontrar_hijos(hijo))
	return hijos

#=========================================================
# Objeto quad tree es un arbol de cuatro ramas por nodo
# para agrupar particulas en cajas y acelerar los calculos
# con n particulas
# Las cajas contienen maximo de k particulas
#==========================================================
class QTree():
	def __init__(mi,k:int, n:int):
		mi.umbral = k
		mi.particulas = [Particula(random.uniform(0,10), random.uniform(0,10)) for x in range(n)]
		mi.root = Nodo(0,0,10,10,mi.particulas)

	def add_particula(mi,x:float, y:float):
		mi.particulas.append(Particula(x,y))

	def get_particulas(mi):
		return mi.particulas

	def subdividir(mi):
		subdivision_recursiva(mi.root,mi.umbral)

	def visualizacion(mi):
		fig = plt.figure(figsize=(12,8))
		plt.title("QuadTree")
		c = encontrar_hijos(mi.root)
		print("Nmero de segmentos: %d" %len(c))
		areas = set()
		for el in c:
			areas.add(el.ancho*el.ancho)
		print("Minima area por segmento: %.3f units" %min(areas))
		for n in c:
			plt.gcf().gca().add_patch(patches.Rectangle((n.x0,n.y0), n.ancho, n.alto, fill = False))
		x = [particula.x for particula in mi.particulas]
		y = [particula.y for particula in mi.particulas]
		plt.plot(x,y, 'ro') #Muestra las particulas como puntos rojos
		plt.show()
		return

#===========================
# Programa principal
#===========================
qtree = QTree(5,1000)
qtree.subdividir()
qtree.visualizacion()

