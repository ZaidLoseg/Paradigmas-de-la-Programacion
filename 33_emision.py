#====================================
#  Zaid Lopez Segura
#====================================
# Matematica Algoritmica
# ESFM IPN
# Septiembre 2024
#===================================

#========================
# Broadcast con MPI
# distribucion de datos
#========================
from mpi4py import MPI
import numpy

#Objeto comunicador 
comm = MPI.COMM_WORLD

#quien soy
rank = comm.Get_rank()

#===========================================
# El proceso 0 tiene datos y los otros no
#===========================================
if rank == 0:
	data = {'key1' : [7,2.72,2+3], 'key2' : ('abc', 'xyz')}
else:
	data = None
#====================================================
# Enviar diccionario a todos los procesos desde root
#====================================================
data = comm.bcast(data,root=0)
print(data)

#======================================
# Ahora mas rapido usando numpy
#======================================
# Tamaño del arreglo
n = 10
if rank == 0:
	#Arreglo de enteros del 0 al n-1
	data = numpy.arange(n, dtype='i')
else:
	#Arreglo vacio de enteros de tamaño n
	data = numpy.empty(n, dtype='i')

#===========================================
# Broadcast pro que indica el tipo de dato
# Optimizando para comuncacion mas rapida
#===========================================
comm.Bcast([data,MPI.INT], root=0)

#====================================
# Asegurarse que todo salio bien
#====================================
for i in range(n):
	assert data[i] == i
print(data)






