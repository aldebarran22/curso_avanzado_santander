"""
Implementación del patrón Fachada para acceder a función de C de bajo nivel
"""

from ctypes import *


class C:
    # Un atajo a la DLL de C
    __libc = cdll.msvcrt

    # Atajo a la función strchr de C
    __strchr = __libc.strchr

    # Atajo a la función strstr de C
    __strstr = __libc.strstr

    @staticmethod
    def strchr(cadena, caracter):
        # Registrar el tipo devuelto:
        C.__strchr.restype = c_char_p
        resul = C.__strchr(cadena.encode("utf8"), ord(caracter))
        if resul:
            return resul.decode("utf8")
        else:
            return resul

    @staticmethod
    def strstr(cadena, subcadena):
        # Registrar el tipo devuelto:
        C.__strstr.restype = c_char_p
        resul = C.__strstr(cadena.encode("utf8"), subcadena.encode("utf8"))
        if resul:
            return resul.decode("utf8")
        else:
            return resul


if __name__ == "__main__":
    resul = C.strchr("hola que tal", "q")
    print(resul)

    resul = C.strchr("hola que tal", "X")
    print(resul)

    resul = C.strstr("hola que tal", "que")
    print(resul)
