"""
Implementa una factoria concreta Samsung.
Se encarga de crear los productos concretos que 
pertenecen a la familia: S20 y GalaxyA
"""

from Factoria import Factoria
from S20 import S20
from GalaxyA import GalaxyA

class FactoriaSamsung(Factoria):

    def createTablet(self):
        return GalaxyA()
    
    def createTno(self):
        return S20()
