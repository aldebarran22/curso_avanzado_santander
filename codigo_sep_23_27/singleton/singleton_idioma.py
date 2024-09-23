"""
Patrón singleton para la carga de un fichero
de idioma
"""


def cargarFichero(idioma):
    path = f"idiomas/{idioma}.txt"
    fich = None
    dicc = dict()
    try:
        fich = open(path, "r")
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition('=')
            dicc[k] = v
        return dicc

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()

if __name__=='__main__':
    dicc = cargarFichero("es")            
    print(dicc)
