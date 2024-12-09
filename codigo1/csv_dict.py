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

def dictToCsv(dicc, sep=';'):
    cabs = sep.join(dicc[0].keys())
    resul = [cabs]
    for d in dicc:
        datos = sep.join(d.values())        
        resul.append(datos)
    return "\n".join(resul)


if __name__ == '__main__':
    nombreFich = "Pedidos"
    txt = cargarFichero(f"../ficheros_curso/merge/{nombreFich}.txt")
    print(txt)
    dicc = csvToDict(txt)
    print(dicc)
    txt2 = dictToCsv(dicc)
    print(txt == txt2)