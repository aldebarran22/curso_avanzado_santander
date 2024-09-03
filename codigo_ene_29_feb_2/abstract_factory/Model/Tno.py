#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc


class Tno(abc.ABC):
    @abc.abstractmethod
    def llamar(self):
        pass
