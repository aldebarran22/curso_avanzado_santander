"""
Cargar ficheros csv y convertirlos a diccionarios
"""

def cargarFichero(path):
    fich = open(path, 'r')
    txt = fich.read()
    fich.close()
    return txt


def csvToDict(texto, sep=';'):
    pass

if __name__ == '__main__':
    txt = cargarFichero("../ficheros_curso/merge/Empleados.txt")
    print(txt)
    dicc = csvToDict(txt)
    print(dicc)