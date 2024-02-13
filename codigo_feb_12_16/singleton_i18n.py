"""
Singleton para almacenar un traductor
"""

def cargaFich(lang="es"):
    fich = None
    try:
        path = f"idiomas/{lang}.txt"
        idioma = dict()
        fich = open(path, "r")
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition("=")
            idioma[k] = v
        return idioma

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()
class Singletoni18n:
    
    @staticmethod
    def getInstance():
        pass

def nuevoCliente():
    print(Singletoni18n.getInstance()['inicio'])

def editarCliente():
    print(Singletoni18n.getInstance()['inicio'])

if __name__ == "__main__":
    d = cargaFich("en")
    print(d)
