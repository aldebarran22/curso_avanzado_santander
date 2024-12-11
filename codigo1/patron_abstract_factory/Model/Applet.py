#!/usr/bin/python
#-*- coding: utf-8 -*-

from Factoria import Factoria
from IPad import IPad
from IPhoneX import IPhoneX

class Applet(Factoria):
    def __init__(self):
        pass

    def crearTno(self ):
        return IPhoneX()

    def crearTablet(self ):
        return IPad()

