"""
Implementación del patrón singleton para la traducción de etiquetas
"""
class SingletonIdioma:

    __diccionario = None
    __idioma = None

    @staticmethod
    def getInstance(idioma):

        if SingletonIdioma.__diccionario is None or idioma != SingletonIdioma.__idioma:
            # Cargar el idioma
            print('Se carga el fichero ...')
            SingletonIdioma.__idioma = idioma
            SingletonIdioma.__diccionario = SingletonIdioma.__cargaFichero(idioma)
        
        return SingletonIdioma.__diccionario
        

    @staticmethod
    def __cargaFichero(idioma):
        fich = None
        dicc = dict()
        try:
            path = f"idiomas/{idioma}.txt"
            fich = open(path, 'r')
            for fila in fich:
                fila = fila.rstrip()
                k, _, v = fila.partition('=')
                dicc[k] = v

            return dicc
        except  Exception as e:
            raise ValueError(f'El idioma {idioma} no está soportado')

        finally:
            if fich:
                fich.close()

if __name__ == '__main__':
    try:
        d = SingletonIdioma.getInstance("en")['inicio']
        print(d)
        d = SingletonIdioma.getInstance("en")['twitter']
        print(d)
        d = SingletonIdioma.getInstance("es")['inicio']
        print(d)
    except  Exception as e:
        print(e)