"""
Conexión a la BD con control de excepciones
"""

import sqlite3

class BaseDatos:
    
    def __init__(self, path):
        pass

    def __del__(self):
        pass

if __name__ == '__main__':
    bd = BaseDatos("../BBDD/empresa3.db")