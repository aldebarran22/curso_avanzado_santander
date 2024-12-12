#!/usr/bin/python
#-*- coding: utf-8 -*-

import abc
class Tno(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def llamar(self):
        pass

