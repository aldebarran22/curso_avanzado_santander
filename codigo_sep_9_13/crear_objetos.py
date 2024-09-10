"""
Formas de crear y copiar objetos en Python
"""


class Punto:

    __slots__ = ("__x", "__y")

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"[{self.__x},{self.__y}]"

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
