"""
Codigo de ejemplo para descargar una URL
"""

import urllib.request as urllib2


def descargaURL(url):
	f = None
	numero = None
	
	try:
		f = urllib2.urlopen(url)                
		numero = int(f.read())
		print (numero)
		
	except Exception as e:
		print("ERROR: ", e)
		
	finally:
		if f != None: f.close()
		return numero

if __name__=='__main__':
	url = 'http://www.dpii.es/files/fich0.txt'
	num = descargaURL(url)
	print('Numero : ', num)
