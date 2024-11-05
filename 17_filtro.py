
#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#================================

#=====================
# Uso de filtros
#=====================

#========================================================
# Hacer una lista de los numeros por arriba del promedio 
#========================================================

# Modulo de estadistica
import statistics

bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#=====================================================================
# Hazme una lista de elementos que cumplan la condicion x > promedio
# filter(dondicion,datos)
#=====================================================================
print(list(filter(lambda x: x > promedio,bigdata)))

#=====================
# limpiar datos
#=====================
paises = ["","Argentina","Brasil","","Chile","Mexico","","Colombia","","","Cuba"]

#===================================
# Filtrar lo que no tiene nada
#===================================
print(list(filter(None,paises)))


