"""
Patrón de creación : Singleton
"""

def cargaIdioma(idioma):
    path = f"idiomas/{idioma}.txt"
    fich = None
    try:
        d = dict()
        fich = open(path, 'r')
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition('=')
            d[k] = v

        print(d)

    except Exception as e:
        print(e.__class__.__name__,e)
    
    finally:
        if fich: fich.close()

if __name__ == '__main__':    
    cargaIdioma("es")
