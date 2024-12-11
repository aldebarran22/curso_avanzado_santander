#!/usr/bin/python
#-*- coding: utf-8 -*-

from Factoria import Factoria
from S24 import S24
from GalaxyA import GalaxyA

class Samsung(Factoria):
    def __init__(self):
        pass

    def crearTno(self):
        return S24()

    def crearTablet(self, ):
        return GalaxyA()

