"""
Mensajes de log con la libreria logging
"""

import logging


def prueba1():
    logging.debug('mensaje de debug')
    logging.info('mensaje de info')
    logging.warning('mensaje de warning')
    logging.error('mensaje de error')
    logging.critical('mensaje de critical')


if __name__ == "__main__":
    prueba1()
