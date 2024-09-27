"""
Patrón fachada para acceder a funciones de C a bajo nivel
"""

from ctypes import *

class C:
    """Patron Fachada para crear un envoltorio de la lib de C"""

    # Variables de clase
    # Guarda la lib de C
    __libc = cdll.msvcrt

    # Mapeo de funciones de C
    __strchr = __libc.strchr
    __strstr = __libc.strstr       

    @staticmethod
    def strchr(cad, char):
        """Envoltorio de la funcion strchr de C"""
        C.__strchr.restype = c_char_p
        return C.__strchr(bytes(cad, 'utf-8'), ord(char))

    @staticmethod
    def strstr(cad, search):
        """Envoltorio de la funcion strstr de C"""
        C.__strstr.restype = c_char_p
        return C.__strstr(bytes(cad, 'utf-8'), bytes(search, 'utf-8'))

if __name__ == '__main__':
    ptr = C.strchr("hola que tal", 'x')
    print(ptr)

    ptr = C.strstr("hola que tal", 'tal')
    print(ptr)
