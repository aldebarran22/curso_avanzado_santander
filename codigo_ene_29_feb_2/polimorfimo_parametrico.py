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
	
	
if __name__ == '__main__':
	func('hola')
	func(888)
	func(8.99)
	a = Clase()
	func(a)
