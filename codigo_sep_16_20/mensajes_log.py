"""
Pruebas con la librería logging
"""

import logging


def mensajesConsola():
    logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")


def mensajesFichero():
    logging.basicConfig(
        filename="../ficheros/ejemplo.log", filemode="a", level=logging.INFO
    )
    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")


def mensajesConFormato():

    # Establecer el nombre del logger
    logger = logging.getLogger("nombre_log")

    # El nivel de mensajes del logger:
    logger.setLevel(logging.DEBUG)

    # Crear el handler: puede ser a consola o a fichero:
    handler = logging.StreamHandler()

    # Configurar el formato de los mensajes de salida
    formato = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Establecer los mensajes del logger:
    handler.setFormatter(formato)

    logger.addHandler(handler)

    logger.debug("mensaje debug")
    logger.info("mensaje info")
    logger.warning("mensaje warning")
    logger.error("mensaje error")
    logger.critical("mensaje critical")


if __name__ == "__main__":
    mensajesConsola()
    # mensajesFichero()
    # mensajesConFormato()
