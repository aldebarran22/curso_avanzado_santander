"""
Conversor de CSV a Json
"""
import json
import os

def cargarCSV(path):
    fich = open(path, "r")
    txt = fich.read().strip()
    fich.close()
    return txt

def grabarJson(path, datos):
    fich = open(path, "w")
    json.dump(datos, fich, indent=4)
    fich.close()


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
    L = [cabs]
    for dicc in datos:
        linea = sep.join(dicc.values())
        L.append(linea)
    return "\n".join(L)


if __name__ == "__main__":
    for f in os.listdir("../ficheros_curso/merge"):
        fichero = f.partition('.')[0]
        path = f"../ficheros_curso/merge/{fichero}.txt"
        pathDestino = f"../ficheros/{fichero}.json"
        txt = cargarCSV(path)
        #print(txt)
        datos = csvJson(txt)
        grabarJson(pathDestino, datos)
        #print(datos)
        txt2 = jsonCsv(datos)
        print(txt == txt2)
