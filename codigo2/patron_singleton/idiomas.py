"""
Patrón singleton para implementar un traductor de etiquetas
"""

def cargarIdioma(idioma):
    path = f"idiomas/{idioma}.txt"
    fich = open(path, 'r')
    dicc = dict()
    for linea in fich:
        linea = linea.rstrip()
        k, _, v = linea.partition('=')
        dicc[k] = v        
    fich.close()
    return dicc


if __name__ == '__main__':
    try:
        cargarIdioma.propiedad = 0
        print(cargarIdioma.__dict__, type(cargarIdioma))
        dicc = cargarIdioma('en')
        print(dicc)
    except Exception as e:
        print(e)

