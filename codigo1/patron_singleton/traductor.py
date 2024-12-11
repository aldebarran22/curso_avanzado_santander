"""
Implementación del patrón singleton para la traducción de etiquetas
"""
class SingletonIdioma:

    __diccionario = None

    @staticmethod
    def getInstance(idioma):

        if SingletonIdioma.__diccionario is None:
            # Cargar el idioma
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
    except  Exception as e:
        print(e)