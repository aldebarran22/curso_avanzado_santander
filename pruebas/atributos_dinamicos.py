class Miclase:
	
	def __init__(self, a,b,c):
		self.a = a
		self.b = b
		self.c = c
		
		
if __name__ == '__main__':
	
	obj = Miclase(1,2,3)
	print(obj.__dict__)
	
	d = {'d':4,'e':5}
	print(d)
	obj.__dict__.update(d)
	print(obj.__dict__)
	
	print(obj.a)
	print(obj.e)
