import pandas as pd
from os import mkdir
from os.path import isdir

def exportarPaises(path, pathDestino):
    if not isdir(pathDestino):
        mkdir(pathDestino)
    
    # Cargar el fichero de pedidos:
    
        

if __name__ == '__main__':
    exportarPaises('../ficheros_curso/merge/Pedidos.txt')