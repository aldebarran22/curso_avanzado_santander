"""
Patrón singleton
"""

from os.path import isfile

def cargaIdioma(idioma):
    path = f"idiomas/{idioma}.txt"
    fich = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")

        fich = open(path, "r")
        for fila in fich:
            print(fila)

    except Exception as e:
        print(e)
        raise e

    finally:
        if fich: fich.close()


cargaIdioma("es")
