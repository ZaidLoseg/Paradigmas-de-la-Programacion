#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#================================

#===================================================
# Graficos usando la tortuga que pinta al caminar
#===================================================
import turtle
tortuga = turtle.Turtle()
tortuga.left(90) # Giro a la izquierda de 90°
tortuga.speed(500) #Velocidad de la tortuga

#=================================
# Con angulos de 90 es un arbol h
#=================================
angulo:float = 90

#=========================================
# el arbol se contruye con recursividad
#=========================================

def arbol(i:float,angulo:float):
	if i<10.0:
		return
	else:
		tortuga.forward(i) #camina i
		tortuga.left(angulo) #gira a la izquierda 90 grados
		arbol(3.0*i/4.25,angulo)
		tortuga.right(2*angulo)
		arbol(3.0*i/4.25,angulo)
		tortuga.left(angulo)
		tortuga.backward(i)

arbol(100,angulo)
turtle.done()

