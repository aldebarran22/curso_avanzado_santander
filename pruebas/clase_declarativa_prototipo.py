class declarativa:
	"""clase declarativa"""
	
	att_de_clase = 42
	
	def __init__(self, name):
		self.name = name
		self.subs = []
		
	def __str__(self):
		return "{} ({})".format(self.name, ",".join(self.subs))
		
	def mostrar(self):
		print(self)
		
def proto__init__(self, name):
	self.name = name
	self.subs = []	
	
def proto__str__(self):
	return "{} ({})".format(self.name, ",".join(self.subs))
	
Prototipo = type("Prototipo", (object,), {
	"__init__": proto__init__,
	"__str__": proto__str__,
	"att_de_clase":42})
	
# Se pueden agregar funciones mas tarde:
def mostrar(self):
	print(self)
	
Prototipo.mostrar = mostrar
		
if __name__ == '__main__':
	d = declarativa("prueba")
	d.mostrar()
	
	p = Prototipo("prueba 2")
	p.mostrar()
	
	
	def mostrar2(self, s):
		print(self,s)
		
	Prototipo.mostrar2 = mostrar2
	
	p.mostrar2("hola")
	
	declarativa.mostrar2 = mostrar2
	
	d.mostrar2("hola")
