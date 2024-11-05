


#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#================================

#==========================================
# yield tranforma la funcion a iterador
#==========================================

def migenerador():
	print("primero")
	yield 10
	print("Segundo")
	yield "20"
	print("tercero")
	yield "hola"

#=====================
# gen es un iterador
#=====================
gen = migenerador()
val1 = next(gen)
print(val1)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)


