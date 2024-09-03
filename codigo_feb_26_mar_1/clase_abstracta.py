import abc

class MiClass(abc.ABC):

	@abc.abstractmethod
	def abstracto1(self):
		pass
	def metodo1(self):
		print()
		
try:
    c = MiClass()
except Exception as e:
	print(e)