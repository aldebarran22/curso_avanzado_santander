"""
Patrón singleton
"""

from os.path import isfile

def cargaIdioma(idioma):
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


if __name__=='__main__':
    try:
        d = cargaIdioma("en")
        print(d)
    except Exception as e:
        print(e)
