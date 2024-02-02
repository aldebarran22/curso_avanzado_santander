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

    @staticmethod
    def strchr(cadena, letra):
        """Busca la posición de letra en cadena
        y devuelve la subcadena hasta el final"""
        pass


if __name__ == "__main__":
    resul = C.strchr("hola que tal", "q")
    print(resul)
