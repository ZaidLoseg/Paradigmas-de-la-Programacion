
#==========================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo basededatos.py : trae el objeto base de datos
#==========================================================

from aplicacion.repositorio.basededatos import baseDeDatos

#=========================================================
# Del directorio aplicacion, el subdirectorio respositorio,
# el archivo s3.py : trae el objeto S3
#=========================================================

from aplicacion.repositorio.s3 import S3

#====================================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#=====================================================================

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#========================================================
# Del directorio aplicacion, el subdeirectorio modelos,
# el archivo usuario.py :  trae el objeto Usuario
#========================================================

from aplicacion.modelos.usuario import Usuario

#==============================================================================
# Del directorio aplicacion, el subdirectorio negocios,
# el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscripciones
#==============================================================================

from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#============================
# Crea el objeto Usuario
#============================

usuario = Usuario("Roberto","Jimenes",18)

#=======================
# crea el objeto s3
#=======================
repositorioS3 = S3("321321321","sd324223","Micubeta")

#=============================================================
# interface inscribirusuario del objeto manejodeinscripciones
#=============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print ("\n")

#===================================
# crear el objeto sistemadearchivos
#===================================

repositorioSistemaDearchivos = SistemaDeArchivos("/home/users")

#=============================================================
# interface inscribirusuario del objeto manejodeinscripciones
#=============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDearchivos)
print ("\n")

#============================
# crear el objeto basededatos
#============================

repositorioBaseDeDatos = baseDeDatos("localhost","admin","admin123")

#=============================================================
# interface inscribirusuario del objeto manejodeinscripciones
#=============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print ("\n")

