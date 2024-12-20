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

    # La función de strstr de C, busca cadenas dentro de cadenas:
    __strstr = __libc.strstr
    # El tipo que devuelve:
    __strstr.restype = c_char_p



    @staticmethod
    def strchr(cadena, letra):
        resul = Fachada.__strchr(cadena.encode('utf8'), ord(letra))
        if resul:
            return resul.decode('utf8')
        else:
            return None
        
    @staticmethod
    def strstr(cadena, subcadena):
        resul = Fachada.__strstr(cadena.encode('utf8'), subcadena.encode('utf8'))
        if resul:
            return resul.decode('utf8')
        else:
            return None
        
class FachadaDLL:

    def __init__(self, path):
        self.path = path
        self.__dll = cdll.LoadLibrary(path)
        print(f'DLL {path} cargada ...')        

    def suma(self, a, b):
        return self.__dll.suma(c_int(a), c_int(b))
    
    def helloWorld(self):
        self.__dll.HelloWorld()
        

def testFachada():
    cad = "hola que tal"        
    resul = Fachada.strchr(cad, 'q')
    if resul:
        print(resul)
    else:
        print('No existe la letra')

    
    resul = Fachada.strstr(cad, 'Que')
    if resul:
        print(resul)
    else:
        print('No existe la palabra')


def testFachadaDLL():
    dll = FachadaDLL("./funciones.dll")
    print("sumar: ", dll.suma(12, 55))
    dll.helloWorld()

if __name__ == '__main__':
   # testFachada()
   testFachadaDLL()