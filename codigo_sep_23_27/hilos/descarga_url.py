"""
Codigo de ejemplo para descargar una URL
"""
from threading import Thread
from queue import Queue
import urllib.request as urllib2


class Download(Thread):

	def __init__(self, ini, fin):
		Thread.__init__(self)
		self.ini = ini
		self.fin = fin

	def run(self):
		for i in range(self.ini, self.fin):
			url = f"http://localhost:8000/fich{i}.txt"
			print(url)
			numero = self.descargaURL(url)
			print(numero)

	def descargaURL(self,url):
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
	pass
