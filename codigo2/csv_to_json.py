"""
Conversor de CSV a Json
"""

def cargarCSV(path):
    fich = open(path, 'r')
    txt = fich.read()
    fich.close()
    return txt

def csvJson(txt, sep=";"):
    lineas = txt.split('\n')
    cabs = lineas[0].split(sep)
    #print(cabs)
    resul = []
    for fila in lineas[1:]:
        valores = fila.split(sep)
        dicc = dict(zip(cabs, valores))
        resul.append(dicc)
        #print(dicc)
    return resul


if __name__ == '__main__':
    fichero = "Empleados"
    path = f"../ficheros_curso/merge/{fichero}.txt"
    txt = cargarCSV(path)
    print(txt)
    csvJson(txt)

