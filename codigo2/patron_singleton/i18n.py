

class Singletoni18n:

    __instance = None
    __idioma = None

    @staticmethod
    def getInstance(idioma):
        if Singletoni18n.__instance == None or Singletoni18n.__idioma != idioma:
            print('Se ha cargado el fichero de ', idioma)
            Singletoni18n.__instance = Singletoni18n.__cargarIdioma(idioma)
        
        return Singletoni18n.__instance
    
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
