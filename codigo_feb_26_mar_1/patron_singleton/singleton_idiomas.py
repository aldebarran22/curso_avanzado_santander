"""
Implementación del patrón singleton
Utilidad para i18n
"""


def cargaFichero(idioma):
    fich = None
    try:
        path = f"idiomas/{idioma}.txt"
        print(f"Cargar el fichero: {path}")
        fich = open(path, "r")
        palabras = dict()
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition("=")
            palabras[k] = v
        return palabras
    
    except  Exception as e:
        print(e)
    finally:
        if fich:fich.close()
    

if __name__ == "__main__":
    d = cargaFichero("fr")
    print(d)
