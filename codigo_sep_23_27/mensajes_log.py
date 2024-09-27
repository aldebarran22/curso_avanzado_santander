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

    # Mostrar mensajes desde debug a critical:
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("mensaje debug")
    logging.info("mensaje info")
    logging.warning("mensaje warning")
    logging.error("mensaje error")
    logging.critical("mensaje critical")


def testFichero():
    # Establecer una configuración

    # Mostrar mensajes desde debug a critical:
    logging.basicConfig(
        filename="../ficheros/fichero.log",
        level=logging.INFO,
        filemode="w",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
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
    # testConsola()
    # test2Consola()
    # testFichero()
    mensajesConFormato()
