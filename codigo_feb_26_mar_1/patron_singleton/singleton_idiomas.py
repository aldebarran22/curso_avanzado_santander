"""
Implementación del patrón singleton
Utilidad para i18n
"""

def cargaFichero(idioma):
    path = f"idiomas/{idioma}.txt"
    print(f'Cargar el fichero: {path}')
    fich = open(path, "r")
    palabras = dict()
    for linea in fich:
        linea = linea.rstrip()
        k, _, v = linea.partition("=")
        palabras[k]=v
    fich.close()
    return palabras

if __name__ == "__main__":
    d = cargaFichero("en")
    print(d)

