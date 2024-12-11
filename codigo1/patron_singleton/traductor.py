"""
Implementación del patrón singleton para la traducción de etiquetas
"""

def cargaFichero(idioma):
    fich = None
    try:
        path = f"idiomas/{idioma}.txt"
        fich = open(path, 'r')
        for fila in fich:
            print(fila)


    except  Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()

if __name__ == '__main__':
    cargaFichero('es')