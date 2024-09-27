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
    # Por defecto muestra los mensajes de W, E y C
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")

def test2Consola():
    # Establecer una configuración
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")

if __name__ == '__main__':
    #testConsola()
    test2Consola()


