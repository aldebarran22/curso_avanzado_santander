from functools import singledispatch

@singledispatch
def func(arg):
	print('Comportamiento por defecto')
	
@func.register(int)
@func.register(float)
def _(arg):
	print('Recibo el numero ',arg)
	
class Clase:
	pass
	
@func.register(Clase)
def _(arg):
	print('un objeto de Clase')
	
@func.register(list)
@func.register(set)
def _(arg):
	print(f'La colección tiene {len(arg)} elementos')
	
if __name__ == '__main__':
	func('hola')
	func(888)
	func(8.99)
	a = Clase()
	func(a)
	func([1,2,3,4])
	func({1,2,3,4})
