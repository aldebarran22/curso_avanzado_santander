"""
Implementación del patrón Fachada para acceder a las
funciones nativas de C
"""

from ctypes import *

class C:

    __libc = cdll.msvcrt

    @staticmethod
    def strchr(cadena, char):
        fun_strchr = C.__libc.strchr
        entero = ord(char)
        cad = cadena.encode('utf-8')
        fun_strchr.restype = c_char_p
        resul = fun_strchr(cad, entero)
        if resul:
            return resul.decode('utf-8')
        else:
            return None
        
if __name__ == '__main__':
    print(C.strchr('nombre','b'))
    print(C.strchr('nombre','x'))
