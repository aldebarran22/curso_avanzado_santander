import math, abc

class Vector3D:
	"""Esta clase tiene cierto parecido a lo que necesitamos, pero
	no la podemos modificar"""
	
	def __init__(self,x=0,y=0,z=0):
		self.__x = x
		self.__y = y
		self.__z = z
		
	def getX(self):
		return self.__x
		
	def getY(self):
		return self.__y

	def getZ(self):
		return self.__z
				
	def productoEscalar(self, vector):
		return self.__x * vector.__x + self.__y * vector.__y + self.__z * vector.__z
		
	def norma(self):
		return math.sqrt(self.__x**2+self.__y**2+self.__z**2)
		
	def __str__(self):
		return str(self.__x)+","+str(self.__y)+","+str(self.__z)
		
		
class Vector2D(abc.ABC):
	"""Clase que tenemos que implementar"""
	
	@abc.abstractmethod
	def getAbcisa(self): 
		pass
	
	@abc.abstractmethod	
	def getOrdenada(self):
		pass
		
	@abc.abstractmethod
	def prod(self, v):
		pass
		
	@abc.abstractmethod
	def magnitud(self):
		# La norma del vector
		pass


class VectorPlano1(Vector2D, Vector3D):
	"""Solución H.Múltiple"""

	def __init__(self, x=0, y=0):
		Vector3D.__init__(self,x,y)
	
	def getAbcisa(self): 
		Vector3D.getX(self)
	
	
	def getOrdenada(self):
		Vector3D.getY(self)
		
	
	def prod(self, v):
		pass
		
	
	def magnitud(self):
		# La norma del vector
		pass

class VectorPlano2(Vector2D):
	"""Solución por composición"""
	
	def __init__(self, x=0, y=0):
		self.v3 = Vector3D(x,y)

	def getAbcisa(self): 
		self.v3.getX()
	
	
	def getOrdenada(self):
		self.v3.getY()
		
	
	def prod(self, v):
		pass
		
	
	def magnitud(self):
		# La norma del vector
		pass


