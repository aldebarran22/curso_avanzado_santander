"""
Singleton para almacenar un traductor
"""

def cargaFich(lang="es"):
    path = f"idiomas/{lang}.txt"
    fich = open(path, "r")
    for linea in fich:
        linea = linea.rstrip()
        print(linea)
    fich.close()

cargaFich()