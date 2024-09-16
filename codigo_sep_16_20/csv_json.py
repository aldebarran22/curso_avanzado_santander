"""
Convertir formato CSV a JSon
"""

path = "../ficheros_curso/merge/Empleados.txt"

def csvJson(csv, sep=";"):
    L = csv.split("\n")
    cabs = L[0]
    resul = []
    for i in L[1:]:
        if len(i) > 0:
            d = dict(zip(cabs.split(sep), i.split(sep)))
            resul.append(d)
    return resul


def leerFichero():
    fich = open(path, "r")
    csv = fich.read()
    fich.close()
    return csv

def jsoncsv(resul, sep=";"):
    cabs = sep.join(resul[0].keys())
    L = [cabs]
    for d in resul:
        linea = sep.join(d.values())
        L.append(linea)
    return "\n".join(L)

if __name__=='__main__':
    csv = leerFichero()
    resul = csvJson(csv)
    print(resul)
    resul2 = jsoncsv(resul)
    print(resul2)