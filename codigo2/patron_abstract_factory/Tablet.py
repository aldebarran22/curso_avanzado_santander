#!/usr/bin/python
#-*- coding: utf-8 -*-

import abc
class Tablet(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def internet(self):
        pass

