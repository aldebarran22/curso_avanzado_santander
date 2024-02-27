"""
Implementación del patrón singleton
Utilidad para i18n
"""


class i18n:

    __palabras = None  # El dicc de claves
    __idioma = None     # El idioma actual

    @staticmethod
    def getInstance(idioma="es"):
        if i18n.__idioma != idioma:
            # Se crea la primera o cuando el idioma
            # Para saber el idioma que tenemos
            i18n.__idioma = idioma
            i18n.__cargaFichero()

        return i18n.__palabras

    @staticmethod
    def __cargaFichero():
        fich = None
        try:
            path = f"idiomas/{i18n.__idioma}.txt"
            print(f"Cargar el fichero: {path}")
            fich = open(path, "r")
            i18n.__palabras = dict()
            for linea in fich:
                linea = linea.rstrip()
                k, _, v = linea.partition("=")
                i18n.__palabras[k] = v
            return i18n.__palabras

        except Exception as e:
            print(e)
        finally:
            if fich:
                fich.close()

def pruebas():
    print(i18n.getInstance('en')['galeria_de_fotos'])

if __name__ == "__main__":
    print(i18n.getInstance()['twitter'])
    print(i18n.getInstance()['facebook'])
    print(i18n.getInstance('en')['instagram'])
    print(i18n.getInstance('en')['facebook'])

    pruebas()
