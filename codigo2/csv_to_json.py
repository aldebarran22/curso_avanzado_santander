"""
Conversor de CSV a Json
"""

def cargarCSV(path):
    fich = open(path, 'r')
    txt = fich.read()
    fich.close()
    return txt


if __name__ == '__main__':
    fichero = "Empleados"
    path = f"../ficheros_curso/merge/{fichero}.txt"
    txt = cargarCSV(path)
    print(txt)

