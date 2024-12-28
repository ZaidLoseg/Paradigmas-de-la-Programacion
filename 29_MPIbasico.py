#====================================
#  Zaid Lopez Segura
#====================================
# Matematica Algoritmica
# ESFM IPN
# Septiembre 2024
#===================================

from mpi4py import MPI

#=============================
# Crear un objeto comunicador
#=============================
comunicadores = MPI.COMM_WORLD

#============================
# Numeros total de procesos
#============================
n_procesos = comunicadores.Get_size()

#================================
# Identificador de este proceso
#================================
quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso ", str(quien_soy), "de ",str(n_procesos))

#=============================
# Si yo soy el cero hago esto
#=============================
if quien_soy == 0:
	print("yo soy el proceso 0")

#==============================
# Si soy el 1 hago esto
#==============================
elif quien_soy == 1:
	print("yo soy el proceso 1")

#=======================================
# si yo no soy ni el 1 ni el 2 hago esto
#=======================================
else:
	print("Yo no soy ninguno de los 2 primeros procesos")




