"""
Implementación del patrón singleton
Utilidad para i18n
"""

def cargaFichero(idioma):
    path = f"idiomas/{idioma}.txt"
    print(f'Cargar el fichero: {path}')
    fich = open(path, "r")
    for linea in fich:
        linea = linea.rstrip()
        print(linea)
    fich.close()

if __name__ == "__main__":
    cargaFichero("en")

