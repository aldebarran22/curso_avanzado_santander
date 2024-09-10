"""
Implementa una factoria concreta Applet.
Se encarga de crear los productos concretos que 
pertenecen a la familia: IPhone y IPad
"""

from Factoria import Factoria
from IPad import IPad
from IPhone import IPhone

class FactoriaApplet(Factoria):

    def createTablet(self):
        return IPad()
    
    def createTno(self):
        return IPhone()