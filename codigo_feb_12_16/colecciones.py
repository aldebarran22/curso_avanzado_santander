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
        #d = [dict(zip(cabs, f.split(";"))) for f in lineas[1:-1]]
        resul = []
        for f in lineas[1:-1]:
            datos = f.split(";")
            d = dict(zip(cabs, datos))
            resul.append(d)
        return resul
    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if fich:
            fich.close()


def dictToCSV(L):
    """Restaura un formato CSV a partir de una lista de dicts"""
    csv = ""
    cabs = ";".join(L[0].keys())
    csv = cabs+"\n"
    for d in L:
        csv += ";".join(d.values())+"\n"
    return csv


if __name__ == "__main__":
    d = csvToDict("ficheros/Empleados.txt")
    print(d)
    txt = dictToCSV(d)
    print(txt)
