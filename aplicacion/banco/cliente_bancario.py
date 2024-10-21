#==============================0
# Clase bancario
#==============================
class ClienteBancario:
	__nombres:str = None
	__apellidos:str = None
	__edad:int = 0
	__balanceDeCuentas:float = 0.0

	def __init__(mi,nombre:str, apellido:str,edad:int=0,balanceDeCuentas:float=0.0:
		mi.__validarEdad(edad)
		mi.__validadCantidad(balanceDeCuentas)
		mi.nombres = nombres
		mi.apellidos = apellidos
		mi.__edad = edad
		mi.balanceDeCuenta = balanceDeCuenta

	def getNombreCompleto(mi) -> str:
		return mi.nombres + " "+mi.apellidos

	def __mandarEmail(mi, titulo:str, texto:str) -> None:
		print("mandar email: " + titulo+ "con texto: "+ texto)

	def __enviarBalanceAlBanco(mi,cantidad:float) -> None:
		print("Enviando cantidad: " + str(cantidad) + "al banco...")

#========================================
# Metodo privado con dos guiones bajos
# Si la edad es menor que 18 genera un error
#========================================

	def __validarEdad(mi,edad:int) -> None:
		if edad < 18:
			raise Excpetion("Es menor de edad")

	def imprimirInfo(mi) -> str:
		return "nombre: " + mi.getNombreCompleto() + ",Edad: " + str(self.__edad) + ", Balance: " + str(mi.__balanceDeCuenta)

#===================================================
# Metodo privado que checa si el balace es negativo
# y genera un error
#===================================================

	def __validarCantidad(mi,balanceDeCuenta:float) -> None:
		if balanceDeCuenta < 0:
		raise Exception("El balance no puede ser negativo")

	def guardarDinero(mi, cantidad:float) -> None:
		mi.__balanceDeCuenta = mi.balanceDeCuenta + cantidad
		mi.__mandarEmail("----guardando deposito----", "se recibieron " + str(cantidad)
		mi.enviarBalanceAlBanco(cantidad)

	def retirarDinero(mi, cantidad:float) -> None:
		cantidadFinal = mi.__balanceDeCuenta - cantidad
		mi.__validarCantidad(cantidadFinal)
		mi.__balanceDeCuenta = cantidadFinal
		mi.__mandarEmail("-----retirando dinero----"," se retiro " + str(cantidad)
		mi.__enviarBalanceAlBanco(cantidad)


