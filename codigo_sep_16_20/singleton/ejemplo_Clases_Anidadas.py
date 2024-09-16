class OnlyOne():

	class __OnlyOne():
		
		def __init__(self, arg):
			self.val = arg

		def __str__(self):
			# Con self, entre comillas invertidas imprime la clase, la ref, y el contenido del obj.
			return self + self.val

	# Inicializar la instancia a vacio:
	instance = None

	def __init__(self, arg):
		
		# Comprueba si se ha creado la instancia:
		if not OnlyOne.instance:
			OnlyOne.instance = OnlyOne.__OnlyOne(arg)
			print("Ha creado un nuevo objeto con ", arg)
			
		else:
			OnlyOne.instance.val = arg
			print("NO crea, asigna el valor ",arg)
			
	def __getattr__(self, name):
		return getattr(self.instance, name)

# Codigo de prueba
x = OnlyOne('sausage')
print("x: ",x)
print()

y = OnlyOne('eggs')
print("y: ",y)
print()

z = OnlyOne('spam')
print("z: ",z)
print() 

print("Volvemos a imprimir x e y: Mantienen el ultimo valor:")
print("x: ",x)
print("y: ",y)
print() 

print("\nx, y, z mantienen en la clase anidada la misma instancia\n")

print("Los objetos creados desde fuera si son distintos")
print(x)
print(y)
print(z)

