"""
Convertir los ficheros csv de una carpeta a json
"""

import pandas as pd
import os

def cambiarFormatosCSVToJson(path, pathDestino, ext):
    L = os.listdir(path)
    cabs = ['nombre','sexo','cuenta']
    for f in L:
        nombreFich, _, extFich = f.partition('.')
        if extFich == ext:
            #df = pd.read_csv()
            path_file = path+f"/{f}"
            df = pd.read_csv(path_file, header=None, names=cabs)
            path_file_destino = pathDestino + f"/{nombreFich}.json"
            df.to_json(path_file_destino, orient="records",indent=4)
            print('Creando: ',path_file_destino)

if __name__ == '__main__':
    cambiarFormatosCSVToJson('../ficheros_curso/names', '../ficheros', 'txt')

