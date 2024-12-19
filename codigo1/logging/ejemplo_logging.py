import logging


def mensajesConsola():
	logging.debug('Traza')
	logging.info('Mensaje de info')
	logging.warning('Mensaje de aviso')
	logging.critical('Mensaje de critical')


def mensajesFichero():	
	logging.basicConfig(filename='example.log', filemode = 'w', level=logging.DEBUG)
	logging.debug('This message should go to the log file')
	logging.info('So should this')
	logging.warning('And this, too')
	
	
if __name__=='__main__':
	#mensajesConsola()
	mensajesFichero()
