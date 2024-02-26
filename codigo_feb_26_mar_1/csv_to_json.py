"""
Convertir un formato CSV a json, y de json a csv
"""


def cargaFich(path, sep=";"):
    fich=None
    try:
        fich = open(path, "r")
        txt = fich.read()
        return txt

    except IOError as e:
        print(e)
    finally:
        if fich:fich.close()
        


def csvToJson(txt):
    pass


def jsonToCSV(L):
    pass


if __name__ == "__main__":
    txt = cargaFich("../ficheros/Empleados.txt")
