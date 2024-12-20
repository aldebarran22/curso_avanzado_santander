"""
Patrón Fachada para acceder a funciones de bajo nivel de C
"""

from ctypes import *

class Fachada:
    """
    Implementa funciones envoltorio para llamar a funciones de C
    """

    # La DLL de las funciones de C
    __libc = cdll.msvcrt

    # La función de strchr de C, busca caracteres dentro de cadenas:
    __strchr = __libc.strchr
    # El tipo que devuelve:
    __strchr.restype = c_char_p

    @staticmethod
    def strchr(cadena, letra):
        resul = Fachada.__strchr(cadena.encode('utf8'), ord(letra))
        if resul:
            return resul.decode('utf8')
        else:
            return None