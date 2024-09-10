"""
Producto abstracto
"""

import abc

class Tno(abc.ABC):

    @abc.abstractmethod
    def llamar(self):
        pass