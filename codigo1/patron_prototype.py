"""
Patrón prototype. 
Implementar dos factorias de prototipos:
a) Inicializa todos los objetos al principio. Después en cada petición clona el prototipo
b) Inicializa los objetos bajo demanda. En la primera petición crea el objeto y luego
lo va clonando.
"""

import abc
import copy

class Prototipo(abc.ABC):
	
	def __init__(self, etiqueta='', color='black'):
		self.etiqueta = etiqueta
		self.color = color
				
	def __str__(self):
		return "etiqueta: " + self.etiqueta + " color: " + self.color
			
	@abc.abstractmethod
	def clone(self):
		pass
	
	
class Circulo(Prototipo):
	
	def __init__(self, etiqueta='circulo', color='black', radio=5.0):
		Prototipo.__init__(self, etiqueta, color)
		self.radio = radio
		
	def __str__(self):		
		return super().__str__() + " radio: " + str(self.radio)
			
	def clone(self):
		return copy.deepcopy(self)
		
	
class Rectangulo(Prototipo):
	
	def __init__(self, etiqueta='rectangulo', color='black', ancho=5.0, alto=10.0):		
		Prototipo.__init__(self, etiqueta, color)
		self.ancho = ancho
		self.alto = alto
		
	def __str__(self):		
		return super().__str__() + 	" ancho: " + str(self.ancho) + " alto: " + str(self.alto)
	
	def clone(self):
		return copy.deepcopy(self)
	
class Triangulo(Prototipo):
	
	def __init__(self, etiqueta='triangulo', color='black', base=2.5, altura=8.0):		
		Prototipo.__init__(self, etiqueta, color)
		self.base = base
		self.altura = altura
		
	def __str__(self):		
		return super().__str__() + 	" base: " + str(self.base) + " altura: " + str(self.altura)
			
	def clone(self):
		return copy.deepcopy(self)
	

class Factoria1:
	"""Inicializa todos los prototipos al principio"""
	pass


class Factoria2:
	"""Inicializa los prototipos bajo demanda, en la primera petición"""
	pass


def test(claseFactoria):

	# Crear la factoria
	factoria = claseFactoria()

	# Imprimir el catálogo de prototipos:
	factoria.print()

	# Solicitar algún prototipo
	fig1 = factoria.get("circulo")
	fig1.radio *= 2
	fig1.color = "green"

	factoria.print()

if __name__ == "__main__":
	test(Factoria1)
	test(Factoria2)

