class A:
	
	def metodo_instancia(self, *args, **kargs):
		return "Esto es un metodo de instancia"
		
	@classmethod
	def metodo_clase(cls, *args, **kargs):
		return "metodo de clase"
		
	@staticmethod
	def metodo_estatico(*args, **kargs):
		return "metodo estatico"
		

if __name__ == '__main__':
	a = A()
	print(a.metodo_instancia())
	print(a.metodo_clase())
	print(a.metodo_estatico())
	
	print(A.metodo_instancia(a))
	print(A.metodo_clase())
	print(A.metodo_estatico())	
	
	A.atributo = 'hola'
	print(a.atributo)
