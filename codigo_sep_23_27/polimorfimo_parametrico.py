from functools import singledispatch

@singledispatch
def func(arg):
	print('Comportamiento por defecto')
	
	
@func.register(int)
@func.register(float)
def _(arg):
	print('Recibo el numero ',arg)
	
@func.register(str)
def _(arg):
	print('Viene la cadena ', arg, ' de long: ', len(arg))
	
@func.register(list)
def _(arg):
	for i in arg:
		print(i)
	
class Clase:
	pass
	
@func.register(Clase)
def _(arg):
	print('un objeto de Clase')
	
	
if __name__ == '__main__':
	func(list('hola'))
	func('hola')
	func(888)
	func(8.99)
	a = Clase()
	func(a)
	func(set(range(10)))
