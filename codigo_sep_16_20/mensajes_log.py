"""
Pruebas con la librería logging
"""

import logging

def mensajesConsola():
    logging.basicConfig(level=logging.ERROR)
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")

def mensajesFichero():
    logging.basicConfig(filename="../ficheros/ejemplo.log", filemode='w',level=logging.ERROR)
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")

    
if __name__ == "__main__":
    #mensajesConsola()
    mensajesFichero()