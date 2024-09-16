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
@func.register(str)
def _(arg):
	print('Elementos de la colección: ', len(arg))
	
if __name__ == '__main__':
	func('hola')
	func(888)
	func(8.99)
	a = Clase()
	func(a)
	func([1,2,3,4,5])
	func({1,2,3,4,5})
	func((1,2,3,4,5))
