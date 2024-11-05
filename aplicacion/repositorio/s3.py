from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#======================================
# S3 es hijo de RepositorioDeUsuarios
#======================================

class S3(RepositorioDeUsuarios):
	__ClientId: str
	__secretKey: str
	__bucket: str

	def __init__(mi, clientId: str, secretKey: str, bucket: str):
		mi.__clientId = clientId
		mi.__secretKey = secretKey
		mi.__bucket = bucket
	
	def abrir(mi)->None:
		print(f"estableciendo conexion a AWS SE {mi.__clientId}:{mi.__secretKey}")

	def guardar(mi, usuario:Usuario) -> None:
		userData = {"nombre": usuario.getNombre(),"apellido":usuario.getApellido(),"edad": usuario.getEdad()}
		print(f"guardando usuario de la bandeja:{mi.__bucket}: {userData}")
	def cerrar(mi) -> None:
		print("cerrando conexion AWS S3")

