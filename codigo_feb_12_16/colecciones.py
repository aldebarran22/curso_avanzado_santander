"""
Repaso de colecciones.
"""


def csvToDict(path):
    """Genera una lista de diccionarios"""
    fich = None
    try:
        fich = open(path, "r")
        csv = fich.read()
        lineas = csv.split("\n")
        cabs = lineas[0].split(";")
        d = [dict(zip(cabs, f.split(";"))) for f in lineas[1:-1]]
        return d
    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if fich:
            fich.close()


def dictToCSV(d):
    return 0


if __name__ == "__main__":
    d = csvToDict("ficheros/Empleados.txt")
    print(d)
