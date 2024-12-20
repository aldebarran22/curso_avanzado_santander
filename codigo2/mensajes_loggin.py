"""
Mensajes de log con la libreria logging
"""

import logging
from datetime import datetime

def prueba1():
    logging.debug('mensaje de debug')
    logging.info('mensaje de info')
    logging.warning('mensaje de warning')
    logging.error('mensaje de error')
    logging.critical('mensaje de critical')

def getFileName(directorio='.', prefijo='mensajes'):
    t = datetime.now()
    cad_fecha = t.strftime('%Y_%m_%d_%H_%M_%S')
    return f"{directorio}/{prefijo}_{cad_fecha}.log"

def prueba2():
    logging.basicConfig(filename=getFileName(), level=logging.DEBUG)
    logging.debug('mensaje de debug')
    logging.info('mensaje de info')
    logging.warning('mensaje de warning')
    logging.error('mensaje de error')
    logging.critical('mensaje de critical')


if __name__ == "__main__":
    prueba2()
