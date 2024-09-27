"""
Codigo de ejemplo para descargar una URL
"""
from threading import Thread
from queue import Queue
import urllib.request as urllib2


def descargaURL(url):
	f = None
	numero = None
	
	try:
		f = urllib2.urlopen(url)                
		numero = int(f.read())
		print (numero)
		return numero
	
	except Exception as e:
		print("ERROR: ", e)
		
	finally:
		if f != None: f.close()
		

if __name__=='__main__':
	url = 'http://localhost:8000/fich10.txt'
	num = descargaURL(url)
	print('Numero : ', num)
