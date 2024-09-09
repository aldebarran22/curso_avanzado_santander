"""
Patrón de creación : Singleton
"""

def cargaIdioma(idioma):
    path = f"idiomas/{idioma}.txt"
    fich = None
    try:
        d = dict()
        fich = open(path, 'r')
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition('=')
            d[k] = v

        return d

    except Exception as e:
        print(e.__class__.__name__,e)
    
    finally:
        if fich: fich.close()

class Singleton:

    __palabras = None
    __idioma = None

    @staticmethod
    def getInstance(idioma="es"):
        
        if Singleton.__palabras is None:
            # Cargar fichero
            pass

        return Singleton.__palabras



if __name__ == '__main__':    
    d = cargaIdioma("es")
    print(d)

    Singleton.getInstance()["inicio"]

