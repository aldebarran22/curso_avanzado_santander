"""
Patrón singleton para implementar un traductor de etiquetas
"""

def cargarIdioma(idioma):
    path = f"../ficheros_curso/idiomas/{idioma}.txt"
    fich = open(path, 'r')
    dicc = dict()
    for linea in fich:
        linea = linea.rstrip()
        k, _, v = linea.partition('=')
        dicc[k] = v        
    fich.close()
    return dicc


if __name__ == '__main__':
    dicc = cargarIdioma('it')
    print(dicc)

