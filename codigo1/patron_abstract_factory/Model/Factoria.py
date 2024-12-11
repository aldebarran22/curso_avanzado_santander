#!/usr/bin/python
#-*- coding: utf-8 -*-

import abc

class Factoria(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def crearTno(self):
        pass

    @abc.abstractmethod
    def crearTablet(self):
        pass

