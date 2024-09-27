"""
Ejemplos de la librería logging para emitir mensajes por la
consola o a un fichero.
Configuración puede ser externa con un fich de config
o en el propio módulo.
Formato de los mensajes: fecha_hora, mensaje, nivel, nombre
del logger.
"""

import logging

def testConsola():
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")

if __name__ == '__main__':
    testConsola()


