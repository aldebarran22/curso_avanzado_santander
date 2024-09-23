"""
Patrón singleton para la carga de un fichero
de idioma
"""


def cargarFichero(idioma):
    path = f"idiomas/{idioma}.txt"
    fich = None
    try:
        fich = open(path, "r")
        for linea in fich:
            print(linea)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()

if __name__=='__main__':
    cargarFichero("es")            
