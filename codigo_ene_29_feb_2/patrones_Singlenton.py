"""
Patrones de creación: Singleton
i18n para una aplicación
"""

def cargaFichero(idioma):
    fich=None
    try:
        claves = dict()
        path = f"idiomas/{idioma}.txt"
        fich = open(path, "r")
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition('=')
            claves[k] = v

        return claves

    except  Exception as e:
        print(e)

    finally:
        if fich: fich.close()


if __name__ == "__main__":
    d = cargaFichero('es')
    print(d)