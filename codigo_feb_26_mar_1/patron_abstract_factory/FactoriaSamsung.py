#!/usr/bin/python
# -*- coding: utf-8 -*-

from Factoria import Factoria
from S20 import S20
from GalaxyA import GalaxyA


class FactoriaSamsung(Factoria):
    def __init__(self):
        pass

    def createTablet(
        self,
    ):
        return GalaxyA()

    def createTno(
        self,
    ):
        return S20()
