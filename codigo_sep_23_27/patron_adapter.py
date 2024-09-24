import math, abc

class Vector3D:
	"""La clase que disponemos pero que no se puede modificar"""
	
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
	"""La interface que tenemos que implementar"""
	
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

class VectorPlano(Vector3D, Vector2D):
	"""Solución por herencia múltiple"""
	
	def __init__(self, x=0, y=0):
		Vector3D.__init__(self, x, y, 0)

	def getAbcisa(self): 
		return Vector3D.getX(self)
		
	def getOrdenada(self):
		return Vector3D.getY(self)
			
	def prod(self, v):
		aux = Vector3D(v.x, v.y, 0)
		return Vector3D.productoEscalar(self, aux)
			
	def magnitud(self):
		# La norma del vector
		return Vector3D.norma(self)

class VectorPlano2(Vector2D):
	"""Solución por composición"""

	def __init__(self, x=0, y=0):
		self.v3 = Vector3D(x,y,0)

	def getAbcisa(self): 
		return self.v3.getX()
		
	def getOrdenada(self):
		return self.v3.getY()
			
	def prod(self, v):
		aux = Vector3D(v.x, v.y, 0)
		return self.v3.productoEscalar(aux)
			
	def magnitud(self):
		# La norma del vector
		return self.v3.norma()
	

if __name__ == '__main__':
	v1 = VectorPlano(1,5)	
	print(v1.magnitud())

	v2 = VectorPlano2(1,5)	
	print(v2.magnitud())
