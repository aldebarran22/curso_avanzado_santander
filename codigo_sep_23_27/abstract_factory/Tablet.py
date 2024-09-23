#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc


class Tablet(abc.ABC):
    @abc.abstractmethod
    def internet(self):
        pass
