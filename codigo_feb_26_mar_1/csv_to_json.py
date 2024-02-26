"""
Convertir un formato CSV a json, y de json a csv
"""


def cargaFich(path):
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        return txt

    except IOError as e:
        print(e)
    finally:
        if fich:
            fich.close()


def csvToJson(txt, sep=";"):
    filas = txt.split("\n")
    cabs = filas[0].split(sep)
    L = [dict(zip(cabs, fila.split(sep))) for fila in filas[1:] if len(fila) > 1]
    return L


def jsonToCSV(L, sep=";"):
    cabs = sep.join(L[0].keys())
    filas = [cabs]
    for d in L:
        filas.append(sep.join(d.values()))
    return "\n".join(filas)


if __name__ == "__main__":
    txt = cargaFich("../ficheros/Empleados.txt")
    L = csvToJson(txt)
    for i in L:
        print(i)
    csv = jsonToCSV(L)
    print(csv)
    """
    col1 = "id;nombre;cargo".split(";")
    col2 = "1;Davolio;Representante de ventas".split(";")
    d = dict(zip(col1, col2))
    print(d)
    """
