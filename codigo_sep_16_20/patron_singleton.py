"""
Patrón singleton
"""

from os.path import isfile


class SingletonIdioma:

    __palabras = None
    __idioma = None

    @staticmethod
    def getInstance(idioma="es"):

        if SingletonIdioma.__palabras is None or SingletonIdioma.__idioma != idioma:
            print("Cargando fichero de: ", idioma)
            SingletonIdioma.__palabras = SingletonIdioma.__cargaIdioma(idioma)
            SingletonIdioma.__idioma = idioma

        return SingletonIdioma.__palabras


    @staticmethod
    def __cargaIdioma(idioma):
        path = f"idiomas/{idioma}.txt"
        fich = None
        d = dict()
        try:
            if not isfile(path):
                raise FileNotFoundError(f"No existe el fichero: {path}")

            fich = open(path, "r")
            for fila in fich:
                fila = fila.rstrip()
                k, _, v = fila.partition("=")
                d[k]=v

            return d

        except Exception as e:        
            raise e

        finally:
            if fich: fich.close()



def funcion():
    print('en funcion')
    print(SingletonIdioma.getInstance()["nombre"])


if __name__=='__main__':
    print(SingletonIdioma.getInstance()["inicio"]) # Carga en la primera llamada.
    print(SingletonIdioma.getInstance()["volver"]) # Utilizan el anterior no carga de nuevo.
    print(SingletonIdioma.getInstance()["nombre"])

    funcion()

