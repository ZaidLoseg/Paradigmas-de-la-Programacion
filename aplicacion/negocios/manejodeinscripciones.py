from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#============================
# Clase ManejoDeInscripciones
# NO TIENE VARIABLES !!!
#=============================
class ManejoDeInscripciones:
	#=================================================================
	# Decorador staticmethod
	# El objeto solo tiene la funcion inscribir al usuario
	# Envuelve la funcion sin llamar variables locales
	# el objeto ManejoDeInscripciones es la interface intercambiable
	#==================================================================
	@staticmethod 
	def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
		print("------> Guardando usuario ... \n")
		repositorioDeUsuarios.abrir()
		repositorioDeUsuarios.guardar(usuario)
		repositorioDeUsuarios.cerrar()

