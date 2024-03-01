"""
Fachada para acceder a funciones de bajo nivel C
"""

from ctypes import *


class C:
    # DLL de C
    __libc = cdll.msvcrt

    # Función puts de C
    __puts = __libc.puts

    @staticmethod
    def puts(cadena):
        C.__puts(cadena.encode("utf8"))


if __name__ == "__main__":
    C.puts("hola que tal")
