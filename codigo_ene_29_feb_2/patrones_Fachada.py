"""
Patrones Estructurales: Fachada
Implementar un patrón Fachada para acceder a las funciones de bajo 
nivel de C.
strstr (cadena, subcadena) -> Devuelve un puntero a donde empieza 
la subcadena en cadena.
strchr (cadena, int/char) -> Devuelve un puntero a donde empieza 
el char dentro de la cadena.
"""
from ctypes import *


class C:
    # La librería de C:DLL
    __libc = cdll.msvcrt

    # Capturar la función strchr de C
    __strchr = __libc.strchr

    # Capturar la función strstr de C
    __strstr = __libc.strstr

    @staticmethod
    def strchr(cadena, letra):
        """Busca la posición de letra en cadena
        y devuelve la subcadena hasta el final"""
        if len(letra) != 1:
            raise ValueError("Letra debe tener un sólo char")

        C.__strchr.restype = c_char_p
        C.__strchr.argtypes = [c_char_p, c_char]
        aux = C.__strchr(cadena.encode("utf-8"), letra.encode("utf-8"))
        if aux != None:
            return aux.decode("utf-8")
        else:
            return None

    @staticmethod
    def strstr(cadena, subcadena):
        """Busca la posición de subcadena en cadena
        y devuelve la subcadena hasta el final"""
        if len(subcadena) <= 1:
            raise ValueError("La subcadena debe tener más de un char")

        C.__strstr.restype = c_char_p
        C.__strstr.argtypes = [c_char_p, c_char_p]
        aux = C.__strstr(cadena.encode("utf-8"), subcadena.encode("utf-8"))
        if aux != None:
            return aux.decode("utf-8")
        else:
            return None
        
if __name__ == "__main__":
    resul = C.strchr("hola que tal", "q")
    print(resul)

    resul = C.strstr("hola que tal", "quetal")
    print(resul)
