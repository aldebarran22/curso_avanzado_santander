"""
Cargar ficheros csv y convertirlos a diccionarios
"""

def cargarFichero(path):
    fich = open(path, 'r')
    txt = fich.read().strip()
    fich.close()
    return txt


def csvToDict(texto, sep=';'):
    lineas = texto.split("\n")
    cabs = lineas[0].split(sep)
    resul = []
    #print(cabs)
    for linea in lineas[1:]:
        datos = linea.split(sep)
        #print(datos)
        dicc = dict(zip(cabs, datos))
        #print(dicc)
        resul.append(dicc)
    return resul

if __name__ == '__main__':
    txt = cargarFichero("../ficheros_curso/merge/Pedidos.txt")
    print(txt)
    dicc = csvToDict(txt)
    print(dicc)