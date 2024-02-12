"""
Repaso de colecciones.
"""


def csvToDict(path):
    """Genera una lista de diccionarios"""
    fich = None
    try:
        fich = open(path, "r")
        csv = fich.read()
        print(csv)
    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if fich:
            fich.close()


def dictToCSV(d):
    pass


if __name__ == "__main__":
    csvToDict("ficheros/Empleados.txt")
