"""
Patrón Abstract Factory.
"""

import abc

class Factoria(abc.ABC):
    """Implementa la factoria genérica. Con un 
    método create por cada tipo de producto (abstracto)"""

    @abc.abstractmethod
    def createTablet(self):
        pass

    @abc.abstractmethod
    def createTno(self):
        pass