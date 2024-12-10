"""
Conversor de CSV a Json
"""


def cargarCSV(path):
    fich = open(path, "r")
    txt = fich.read().strip()
    fich.close()
    return txt


def csvJson(txt, sep=";"):
    lineas = txt.split("\n")
    cabs = lineas[0].split(sep)
    # print(cabs)
    resul = []
    for fila in lineas[1:]:
        valores = fila.split(sep)
        dicc = dict(zip(cabs, valores))
        resul.append(dicc)
        # print(dicc)
    return resul


def jsonCsv(datos, sep=";"):
    """
    Recibe una lista de dicc. y los convierte a un formato CSV
    """
    cabs = sep.join(datos[0].keys())
    print(cabs)


if __name__ == "__main__":
    fichero = "Empleados"
    path = f"../ficheros_curso/merge/{fichero}.txt"
    txt = cargarCSV(path)
    print(txt)
    datos = csvJson(txt)
    print(datos)
    jsonCsv(datos)
