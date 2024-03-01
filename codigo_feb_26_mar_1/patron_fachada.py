"""
Fachada para acceder a funciones de bajo nivel C
"""

from ctypes import *


class C:
    # DLL de C
    __libc = cdll.msvcrt

    # Función puts de C
    __puts = __libc.puts

    # Función strchr de C
    __strchr = __libc.strchr

    # Función de strstr de C
    __strstr = __libc.strstr

    @staticmethod
    def puts(cadena):
        C.__puts(cadena.encode("utf8"))

    @staticmethod
    def strchr(cadena, letra):
        C.__strchr.restype = c_char_p
        resul = C.__strchr(cadena.encode("utf8"), ord(letra))
        return resul.decode('utf8') if resul != None else None
    
    @staticmethod
    def strstr(cadena, subcadena):
        C.__strstr.restype = c_char_p
        C.__strstr.argtypes = [c_char_p, c_char_p]
        resul = C.__strstr(cadena.encode("utf8"), subcadena.encode("utf8"))
        return resul.decode('utf8') if resul != None else None

if __name__ == "__main__":
    C.puts("hola que tal")

    print(C.strchr("hola que tal", "x"))
    print(C.strchr("hola que tal", "t"))

    print(C.strstr("hola que tal", "adios"))
    print(C.strstr("hola que tal", "que"))