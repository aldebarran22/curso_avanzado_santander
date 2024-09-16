"""
Convertir formato CSV a JSon
"""

path = "../ficheros_curso/merge/Empleados.txt"

def csvJson(csv):
    L = csv.split("\n")
    cabs = L[0]
    resul = []
    for i in L[1:]:
        if len(i) > 0:
            d = dict(zip(cabs.split(";"), i.split(";")))
            resul.append(d)
    return resul


def leerFichero():
    fich = open(path, "r")
    csv = fich.read()
    fich.close()
    return csv

def jsoncsv(resul):
    pass

if __name__=='__main__':
    csv = leerFichero()
    resul = csvJson(csv)
    print(resul)