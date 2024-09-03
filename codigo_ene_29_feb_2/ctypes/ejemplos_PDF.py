from ctypes import *

# Cargar las librerias:
libc = cdll.msvcrt

# Definir un atajo para printf
printf = libc.printf 

# Pruebas con las funciones de C
print("\nLLAMADA A FUNCIONES DE C")
printf("%s %d %f\n\n", "hola", c_int(67), c_double(8.99))
# libc.printf("%s %d %f\n\n", "hola", 67, 8.99) ERROR
print()


# Llamada a funciones con tipos personalizados:
class Bottles(object): 

	def __init__(self, number):  
		self._as_parameter_ = number 
	
bottles = Bottles(42) 
print("\nLLAMADA CON TIPOS PERSONALIZADOS")
printf("%d bottles ", bottles) 
print()
print()

# Pruebas para especificar los tipos de los parametros de la funciOn
print("\nESPECIFICANDO TIPOS ANTES DE LLAMAR A LA FUNCION")
printf.argtypes = [c_char_p, c_char_p, c_int, c_double] 
printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2) 


# Pruebas con los tipos devueltos:
print ("\nTIPOS DEVUELTOS")
strchr = libc.strchr
# Hay que indicar el tipo devuelto si no, devuelve un numero que es la dir. del ptr:
print(strchr(b"abcdef", ord("d")))
strchr.restype = c_char_p # c_char_p es un puntero a string
print(strchr(b"abcdef", ord("d"))) 
print(strchr(b"abcdef", ord("x"))) 

# Ambas situaciones: especificando tipo de retorno y argumentos
print("\nESPECIFICANDO TIPO DE RETORNO Y DE LOS ARGUMENTOS")
strchr.restype = c_char_p
strchr.argtypes = [c_char_p, c_char]
print(strchr(b"abcdef", b"d"))

# Paso de parametros por referencia:
print("\nPASO DE PARAMETROS POR REFERENCIA")
i = c_int()
f = c_float()
s = create_string_buffer(b'\000' * 32)
print(i.value, f.value, repr(s.value))
libc.sscanf(b"1 3.14 Hello", b"%d %f %s", byref(i), byref(f), s)
print(i.value, f.value, repr(s.value))


#Estructuras
print("\nPRUEBA CON ESTRUCTURAS")
class POINT(Structure):
	_fields_ = [("x", c_int),("y", c_int)]
	
point = POINT(10, 20)
print(point.x, point.y)

point = POINT(y=5)
print(point.x, point.y)

print("\nANIDANDO ESTRUCTURAS")
class RECT(Structure):
	_fields_ = [("upperleft", POINT),("lowerright", POINT)]

rc = RECT(point)
print(rc.upperleft.x, rc.upperleft.y)
print(rc.lowerright.x, rc.lowerright.y)

# Se puede inicializar asi:
r = RECT(POINT(1, 2), POINT(3, 4))
r = RECT((1, 2), (3, 4))


# Arrays
print("\nUN ARRAY DE ENTEROS")
TenIntegers = c_int * 10
ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ii)
for i in ii: 
	print(i, end= " ")
print() 

# Punteros:
print("\nPUNTEROS")
n = c_int(40)
pi = pointer(n)
print(pi)
print(pi.contents)


print()
