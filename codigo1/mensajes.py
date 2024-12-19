"""
Pruebas con la librería de logging
"""

import logging


def mensajes1():
    """Configuración por defecto, sin cambiar nada.
    El mínimo es warning (no muestra ni debug ni info)"""
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")


def mensajes2():
    """Configuración a un fichero de mensajes. Por defecto el fichero se extendiende cada
    que ejecutas la función: modo 'w' """
    logging.basicConfig(filename="../ficheros/mensajes.log",filemode='w', level=logging.INFO)
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")

def mensajes3():
    """Configuración a un fichero de mensajes, añadiendo filas al final"""
    logging.basicConfig(filename="../ficheros/mensajes3.log",  level=logging.INFO)
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")


def mensajes4():
    """Configuración a un fichero y volcando la fecha/hora, el mensaje y el nivel"""
    logging.basicConfig("../ficheros/mensajes4.log", 
                        format="%(asctime)s\t%(levelname)s\t%(message)s",
                        datefmt="%d-%b-%Y %H:%M:%S", level=logging.DEBUG)
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")

if __name__ == "__main__":
    # mensajes1()
    # mensajes2()
    # mensajes3()
    mensajes4()