

class Singletoni18n:

    __instance = None

    @staticmethod
    def getInstance(idioma):
        pass
    
    @staticmethod
    def __cargarIdioma(idioma):
        path = f"idiomas/{idioma}.txt"
        fich = open(path, 'r')
        dicc = dict()
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition('=')
            dicc[k] = v        
        fich.close()
        return dicc
