# Cargar una DLL y llamar a las funciones
#int sumar(int, int)
#int restar(int, int)

# OJO DESDE EL DEV-CPP GENERAR LA DLL DE 32 BITS!

from ctypes import *

# Indicar el path de la DLL
miDLL = cdll.LoadLibrary("dll2.dll")

suma = miDLL.suma(c_int(3), c_int(4))
resta = miDLL.resta(c_int(8), c_int(9))

print("Suma: ", suma)
print("Resta: ", resta)
miDLL.HelloWorld()
