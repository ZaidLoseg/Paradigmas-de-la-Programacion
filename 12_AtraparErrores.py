


#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#================================ 

#====================================================
# La clase ClienteBancario esta en el subdirectorio
# aplicacion/banco/
#=====================================================
from aplicacion.banco.cliente_bancario import ClienteBancario

#==========================================
# try: intenta (correr las instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir en string
#===========================================

#============================================
# Error por sacar mas dinero del que tiene
#============================================
try:
	cliente = ClienteBancario("Jamime Andrade","Hernandez Sanchez",28,0.0)
	cliente.guradarDinero(300)
	print(cliente.imprimirInfo())
	cliente.retirarDinero(400)
	print(cliente.imprimirInfo())
#=============================================
# Excepcion es el objeto mas general de error
#=============================================
except Exception as e:
	print("Error: " + str(e))

#====================================
# Error por usar un atributo privado
#====================================
try:
	print(cliente.__nombres)
except exception as ex:
	print("Error: " + str(ex))

#====================
# Forma correcta
#====================
print(cliente.nombres)

