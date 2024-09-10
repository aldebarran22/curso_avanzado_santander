"""
Implementa una factoria concreta.
Se encarga de crear los productos concretos que 
pertenecen a la familia.
"""

from Factoria import Factoria
from S20 import S20
from GalaxyA import GalaxyA

class FactoriaSamsung(Factoria):

    def createTablet(self):
        return GalaxyA()
    
    def createTno(self):
        return S20()
