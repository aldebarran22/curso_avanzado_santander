"""
Patrón de creación : Singleton
"""


class Singleton:

    __palabras = None
    __idioma = None

    @staticmethod
    def getInstance(idioma="es"):
        
        if Singleton.__palabras is None or Singleton.__idioma != idioma:
            # Cargar fichero
            print(f'Cargamos el fichero de {idioma}')
            Singleton.__palabras = Singleton.__cargaIdioma(idioma)
            Singleton.__idioma = idioma
            
        return Singleton.__palabras
    
    @staticmethod
    def __cargaIdioma(idioma):
        path = f"idiomas/{idioma}.txt"
        fich = None
        try:
            d = dict()
            fich = open(path, 'r')
            for linea in fich:
                linea = linea.rstrip()
                k, _, v = linea.partition('=')
                d[k] = v

            return d

        except Exception as e:
            print(e.__class__.__name__,e)       
        
        finally:
            if fich: fich.close()

if __name__ == '__main__':        
    print(Singleton.getInstance()["inicio"])
    print(Singleton.getInstance()["volver"])
    print(Singleton.getInstance()["nombre"])

