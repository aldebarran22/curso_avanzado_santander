#!/usr/bin/python
# -*- coding: utf-8 -*-

from Factoria import Factoria
from IPad import IPad
from IPhone import IPhone


class FactoriaApple(Factoria):
    def __init__(self):
        pass

    def createTablet(
        self,
    ):
        return IPad()

    def createTno(
        self,
    ):
        return IPhone()
