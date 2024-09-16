"""
Convertir formato CSV a JSon
"""

path = "../ficheros_curso/merge/Empleados.txt"

def csvJson(csv):
    print(csv)

def leerFichero():
    fich = open(path, "r")
    csv = fich.read()
    fich.close()
    return csv

if __name__=='__main__':
    csv = leerFichero()
    csvJson(csv)