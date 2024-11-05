#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#=================================

#========================================
# Uso de reducciones (colapsar resultado)
#========================================

#=================================================
# Multiplicacion de todos los numeros de la lista
#=================================================

from functools import reduce

bigdata = [2,3,5,7,11,13,17,19,23,29]

#=================
# Funcion x*y
#=================
multiplicar = lambda x,y: x*y
suma = lambda x,y: x+y

print(reduce(multiplicar,bigdata))
print(reduce(suma,bigdata))

#============================================================
# Reduce la aplica la funcion por pares a los resultados y 
# el siguiente elemento comenzando con los dos primeros 
# elementos
#============================================================
