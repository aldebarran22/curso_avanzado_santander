from ctypes import *

# Indicar el path de la DLL
C = cdll.msvcrt
print('Lib. de C')
print(C)
print()


# Hacer llamadas a las funciones de C:
print('Dir. de la funcion printf:')
print(C.printf)

C.printf(b"\nPrueba: %s\n", b"PRUEBA")

C.printf(b"\nVariables: %s %d %g\n", b"Cadena", c_int(100), c_double(8.99))

s = b"Cadena de caracteres"
i = c_int(C.strlen(s))
C.printf(b"\nLa cadena %s tiene %d chars.\n", s, i)

s = input('Cadena de texto: ')
ss = s.encode('utf-8')
i = c_int(C.strlen(ss))
C.printf(b"\nLa cadena %s tiene %d chars.\n", ss, i)







