"""
Seleccionar la factoria del AbstractFactory
a partir de un menú dinámico o con la linea de comandos
"""

import sys
from Factoria import Factoria
from FactoriaApple import FactoriaApple
from FactoriaSamsung import FactoriaSamsung

print(sys.argv)
print(Factoria.__subclasses__())
