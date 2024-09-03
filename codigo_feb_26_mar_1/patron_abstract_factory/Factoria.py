#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc


class Factoria(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def createTablet(
        self,
    ):
        pass

    @abc.abstractmethod
    def createTno(
        self,
    ):
        pass


if __name__ == "__main__":
    try:
        f = Factoria()
    except Exception as e:
        print(e)
