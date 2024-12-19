#====================================
#  Zaid Lopez Segura
#====================================
# Matematica Algoritmica
# ESFM IPN
# Septiembre 2024
#===================================

#==============================
# Importar Numba, numpy y time
#==============================
from numba import jit
import numpy
import time

#================================
# loop cualquiera en phyton puro
#================================
def lento(a):
	t = 0.0
	# Para cada renglon
	for i in range(a.shape[0]):
		t += numpy.tanh(a[i,i])
	return a + t

#=========================
# Loop sin interprete
#=========================
@jit(nopython=True)
def rapido(a):
	t=0.0
	for i in range(a.shape[0]):
		t += numpy.tanh(a[i,i])
	return a + t

#==================================================
# Arreglo unidimensional lleno del 1 al 10000 
# convertido en matriz de 100x100
#==================================================
x = numpy.arange(10000).reshape(100,100)

#=====================================================
# La primera llamada incluye el tiempo de compilacion
#=====================================================
start = time.time()
rapido(x)
end = time.time()
print("Tiempo incluyendo compilacion = %s" % (end-start))

#==============================================================
# La seguna llamada es para obetenr el tiempo de ejecucion
#==============================================================
start = time.time()
rapido(x)
end = time.time()
print("Tiempo usando numba = %s" % (end-start))	

#==============================================
# Tiempo para la funcion sin optimizacion
#==============================================
start = time.time()
lento(x)
end = time.time()
print("Tiempo usando python puro = %s" % (end-start))
