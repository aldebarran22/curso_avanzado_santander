"""
Implementación del patrón builder:
Objetivo convertir un fichero CSV a distintos formatos:
XML -> BuilderXML
HTML -> BuilderHTML
JSon -> BuilderJSon
"""

import abc

class Builder(abc.ABC):
    """Define las operaciones genéricas que hay que implementar
    en un builder"""

    