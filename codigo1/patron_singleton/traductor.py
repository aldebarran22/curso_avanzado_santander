"""
Implementación del patrón singleton para la traducción de etiquetas
"""

def cargaFichero(idioma):
    fich = None
    dicc = dict()
    try:
        path = f"idiomas/{idioma}.txt"
        fich = open(path, 'r')
        for fila in fich:
            fila = fila.rstrip()
            k, _, v = fila.partition('=')
            dicc[k] = v

        return dicc
    except  Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()

if __name__ == '__main__':
    d = cargaFichero('es')
    print(d)