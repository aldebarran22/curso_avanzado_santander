"""
Singleton para almacenar un traductor
"""


class Singletoni18n:

    __idioma = None  # El idioma actual
    __palabras = None  # El diccionario para traducir etiquetas

    @staticmethod
    def getInstance(idioma="es"):
        if Singletoni18n.__idioma != idioma:
            print("Carga fichero ...")
            Singletoni18n.__idioma = idioma
            # Cargar fichero.
            Singletoni18n.__cargaFich()

        return Singletoni18n.__palabras

    @staticmethod
    def __cargaFich():
        fich = None
        try:
            path = f"idiomas/{Singletoni18n.__idioma}.txt"
            Singletoni18n.__palabras = dict()
            fich = open(path, "r")
            for linea in fich:
                linea = linea.rstrip()
                k, _, v = linea.partition("=")
                Singletoni18n.__palabras[k] = v

        except Exception as e:
            print(e)
        finally:
            if fich:
                fich.close()


def nuevoCliente():
    print(Singletoni18n.getInstance()['inicio'])


def editarCliente():
    print(Singletoni18n.getInstance("en")['inicio'])
    print(Singletoni18n.getInstance("en")['twitter'])


if __name__ == "__main__":
    nuevoCliente()
    nuevoCliente()
    editarCliente()
