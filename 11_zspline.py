


#=================================
# Zaid Lopez Segura
#=================================
#  Paradigmas de la Programacion
#  Matematicas Algoritmicas
#  ESFM-IPN    sept-2025
#================================
# CURVAS Z-SPLINES EN N DIMENSIONES
#================================

import numpy as np
from Curva import Curva,zspline
import matplotlib.pyplot as plt
import math

#=======================
# Conjunto de puntos
#=======================
# Numero de puntos
nump:np.int32 = 8
# Dimension
dim:np.int32 = 2
# Meromoria para puntos
puntos = np.zeros(dim*nump,dtype=np.float64)
#Parametrizacion
X = np.linspace(0.0,2*np.pi,nump+1)
#Coordenada x
puntos[0:nump] = np.cos(X[0:nump]) + 0.0*np.sin(2*X[0:nump])
#Coordenadas y
puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

#==============================================================
# Curvas z-spline de n puntos zspline(p,d,n,m)
# p: puntos, d: dimension, n: segmentos de curva, m: continuidad
#===============================================================

n:np.int32 = 100
x1,y1 = zspline(puntos,dim,n,2)
x2,y2 = zspline(puntos,dim,n,1)
x3,y3 = zspline(púntos,dim,n,0)
plt.plot(x3,y3,lw=3,color="orange")
plt.plot(x2,y2,lw=3,color="red")
plt.plot(x1,y1,lw=3,color="blue")
plt.scatter(puntos[0:nump],puntos[nump:2*nump],marker='o', color="black")
plt.xlable("coordenadas x")
plt.ylabel("coordenadas y")
plt.title("curva cerrada z-spline en 2D")
plt.show()


