class Reversa:
	"""Iterador para recorrer una secuencia marcha atrás."""
	def __init__(self, datos):
		self.datos = datos
		self.indice = len(datos)
     
	def __iter__(self):	
		return self
		
	def __next__(self):
		if self.indice == 0:
			self.indice = len(self.datos) # Para volver a repetir
			raise StopIteration
		
		self.indice = self.indice - 1
		return self.datos[self.indice]


rev = Reversa('spam')
print(iter(rev))
for char in rev:
	print(char)
	
	
for char in rev:
	print(char)
	
for char in rev:
	print(char)	
