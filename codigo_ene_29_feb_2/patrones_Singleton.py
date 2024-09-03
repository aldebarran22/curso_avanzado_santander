"""
Patrones de creación: Singleton
i18n para una aplicación
"""


def cargaFichero(idioma):
    fich = None
    try:
        claves = dict()
        path = f"idiomas/{idioma}.txt"
        fich = open(path, "r")
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition("=")
            claves[k] = v

        return claves

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


class Singletoni18n:
    """
    Patrón Singleton, limitar el número de cargas de un fichero de
    idiomas
    """

    __palabras = None  # El diccionario con las claves
    __idioma = None  # El idioma actual

    @staticmethod
    def getInstance(idioma="es"):
        # Comprobar si tenemos que cargar el fichero:
        if Singletoni18n.__idioma != idioma:
            print('Se actualiza el idioma')
            Singletoni18n.__palabras = cargaFichero(idioma)
            Singletoni18n.__idioma = idioma

        # Si no se producen cambios devolvemos la última versión del idioma
        return Singletoni18n.__palabras


if __name__ == "__main__":
    # Prueba de la carga del fichero
    d = cargaFichero("es")
    print(d)

    print(Singletoni18n.getInstance()["facebook"])
    print(Singletoni18n.getInstance("es")["inicio"])
    print(Singletoni18n.getInstance('en')["twitter"])
