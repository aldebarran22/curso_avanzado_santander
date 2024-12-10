"""
Patrón singleton para implementar un traductor de etiquetas
"""

def cargarIdioma(idioma):
    path = f"../ficheros_curso/idiomas/{idioma}.txt"
    fich = open(path, 'r')
    for linea in fich:
        print(linea)
    fich.close()


if __name__ == '__main__':
    cargarIdioma('en')

