import math
import abc

class Vector3D:
	
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


class VectorPlano(Vector2D,Vector3D):
	"""Solución con herencia múltiple"""
	
	def __init__(self,a=0,b=0):
		Vector3D.__init__(self, a, b, 0)
		
	def getAbcisa(self):
		return Vector3D.getX(self)
		
	def getOrdenada(self):
		return Vector3D.getY(self)
		
	def prod(self, v):
		v_3d = Vector3D(v.getAbcisa(), v.getOrdenada(), 0)	
		return Vector3D.productoEscalar(self,v_3d)		
		
	def magnitud(self):
		return Vector3D.norma(self)
		
	def __str__(self):
		return str(Vector3D.getX(self))+","+str(Vector3D.getY(self))
		

class VectorPlano2(Vector2D):
	"""Solución 2: Utilizando composición"""
	
	def __init__(self, a=0, b=0):
		self.__v3d = Vector3D(a,b,0)
				
	def getAbcisa(self):
		return self.__v3d.getX()
		
	def getOrdenada(self):
		return self.__v3d.getY()
		
	def prod(self, v):
		v_3d_2 = Vector3D(v.getAbcisa(), v.getOrdenada(), 0)		
		return self.__v3d.productoEscalar(v_3d_2)		
		
	def magnitud(self):
		return self.__v3d.norma()	
		
	def __str__(self):
		return str(self.__v3d.getX())+","+str(self.__v3d.getY())		
				
		
def main():
	# Prueba con la version de Herencia Multiple
	v1 = VectorPlano(3,4)
	v2 = VectorPlano(8,7)

	print("v1",v1)
	print("v2",v2)
	print("La norma del vector (3,4) es: ",v1.magnitud())
	print("El producto de los vectores (3,4) y (8,7) es : ", v1.prod(v2))

	print() 
	
	# Prueba con la version de Composicion
	v3 = VectorPlano2(3,4)
	v4 = VectorPlano2(8,7)


	print("v3",v3)
	print("v4",v4)
	print("La norma del vector (3,4) es: ",v3.magnitud())
	print("El producto de los vectores (3,4) y (8,7) es : ", v4.prod(v3))
	
if __name__ == "__main__":
	main()		
