#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#=================================



#=====================
# Operaciones Basicas
#=====================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5)  # raiz cuadrada
print (10%2)
print (10%0.1)

#=========================================
# Para saber el tipo de objeto se usa type
#=========================================
t=0
print(type(t)) #entero
t=3.6
print(type(t)) #flotante
t=True
print(type(t)) #booleano

#=====================
# Mensajes en pantalla
#=====================
print("Este es un comando de phyton. ","Este es otro enunciado. ",t)
print('id: ',1)
print('Nombres: ','Steve')
print('Apellidos: ', 'Jobs')
print("vamos a sumar esto" + "con esto otro")

#=============================================
# CONTINUAR UNA INTRUCCION EN VARIOS RENGLONES
#=============================================
if 100 > 99 and \
  200 <= 300  and \
  True != False:
       print('¡Hola a todos!')

#==========================================
# DIFERENTES COMANDOS EN UNA SOLA LINEA
#==========================================
print ("Hola "); print ("tu")

#===============================================
# USANDO PARENTESIS REDONDOS,CUADRADOS O LLAVES
# SE PUEDE ESCRIBIR EN VARIOS RENGLONES
#===============================================

lista = [1, 2, 3, 4,
	5, 6, 7, 8,
	9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]
print(lista)
print(matriz)

#===================================================
#IDENTACION ESTRICTA PARA PROCESOS DEPENDIENTES DE :
#===================================================
if 10>5
  print("diez es mayor que cinco")
  print("otra identacion")
for i in lista:
  print (i)
  print ("ok")
if 10>5:
  print ("verdadero")
  if 10<20:
    print("verdadero")
elif 5>3
  print ("Esto no se imprimira")
else:
  print("aqui nunca llega")

#==========
#FUNCIONES 
#==========
def saludar(nombre)
    print("Hola ",nombre)
    print("Bienvenido al tutorial de phyton")

saludar(julian)
