"""
Patrón singleton para la carga de un fichero
de idioma
"""

class SingletonIdioma:

    # Variable de clase:
    __palabras = None
    __idioma = None

    @staticmethod
    def getInstance(idioma='es'):

        if SingletonIdioma.__palabras is None or SingletonIdioma.__idioma != idioma:
            # Es la primera vez o hay un cambio de idioma:
            print("Carga del fichero: "+idioma)
            SingletonIdioma.__palabras = SingletonIdioma.__cargarFichero(idioma)
            SingletonIdioma.__idioma = idioma
        
        return SingletonIdioma.__palabras

    @staticmethod
    def __cargarFichero(idioma):
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
            raise e
        
        finally:
            if fich:
                fich.close()

#if __name__=='__main__':
   
