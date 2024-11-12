#====================================
#  Zaid Lopez Segura
#====================================
# Matematica Algoritmica
# ESFM IPN
# Septiembre 2024
#====================================

#=====================================
# Funcion que regresa otra funcion
#=====================================
def uppercase_decorator(function):
	def wrapper():
		fun = function()
		make_uppercase = fun.upper()
		return make_uppercase

	return wrapper

#================
# Funcion saludo
#================
def say_hi():
	return 'hello there'

#================================
# Generar y correr saludo
#================================
decorate = uppercase_decorator(say_hi)
print(decorate())

#===========================
# Utilizar como decorador
#===========================
@uppercase_decorator
def say_hi():
	return 'hello there'

#======================================
# correr funcion pasada pro decorador
#======================================
print(say_hi())

