#====================================
#  Zaid Lopez Segura
#====================================
# Matematica Algoritmica
# ESFM IPN
# Septiembre 2024
#===================================

from mpi4py import MPI
import numpy 

comm= MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# un dato
data = (rank+1)**2
#===============================================
# Manden sus datos al proceso root=0 (en orden)
#===============================================
datas = omm.gather(data, root=0)

#================================
# Asegurarse que todo funcione
#================================
if rank == 0:
	for i in range(size):
		assert datas[i] == (i+1)**2
else:
	assert datas is None
print(datas)

#============================
# ahora mas rapido con numpy
#============================
n = 10
#========================================
# Arreglo de ceros de tamaño n
# sumando con un escalar (en cada entrada)
#=========================================
sendarray = numpy.zeros(n, dtype='i')+rank
recvarray = None
if rank ==0:
	#======================================
	# Matriz vacia de tamaño procesos*n
	# dtype es el tipo de dato (i) es entero
	#=======================================
	recvarray = numpy.empty([size, n], dtype='i')
#=================================
# Gather es mas rapido para numpy
# enviar datos al proceso root
#=================================
comm.Gather(sendarray, recvarray, root=0)
if rank == 0:
	for i in range(size):
		#=====================
		# revisar por fila
		#====================
		assert numpy.allclose(recvarray[i,:],i)
print(recvarray)




