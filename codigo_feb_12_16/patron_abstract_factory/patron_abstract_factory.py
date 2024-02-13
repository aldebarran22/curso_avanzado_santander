"""
Implementación patrón abstract factory:
2 Familias: Samsung y Apple
2 productos: Tno y Tablet
"""

import abc
from IPad import IPad
from IPhone import IPhone
from S20 import S20
from GalaxyA import GalaxyA


# Factorias
class Factoria(abc.ABC):

    @abc.abstractmethod
    def createTno(self):
        pass

    @abc.abstractmethod
    def createTablet(self):
        pass


class FactoriaSamsung(Factoria):
    """
    Implementan los métodos abstractos y crean
    productos concretos.
    """

    def createTno(self):
        return S20()

    def createTablet(self):
        return GalaxyA()


class FactoriaApple(Factoria):

    def createTno(self):
        return IPhone()

    def createTablet(self):
        return IPad()


# Productos:
class Tno(abc.ABC):

    @abc.abstractmethod
    def llamar(self):
        pass


class Tablet(abc.ABC):

    @abc.abstractmethod
    def internet(self):
        pass
