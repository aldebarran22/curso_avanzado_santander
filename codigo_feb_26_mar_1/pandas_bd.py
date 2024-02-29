"""
Extraer datos (DF) de una BD con pandas y exportar a JSON
"""

import pandas as pd
from os.path import isfile
import sqlite3 as dbapi

class BaseDatos:
     
    def __init__(self, path):
        
        if not isfile(path):
            raise FileNotFoundError("No se encuentra el fichero: "+path)
        else:
            self.con = dbapi.connect(path)
            #print('Base de datos abierta!')

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()