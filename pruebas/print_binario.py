'''
formatear datos binarios:
'''

# No pone los ceros
num1 = 0x0F
print(bin(num1))


# Tampoco pone los ceros
print("{0:b}".format(num1))

print("{0:08x}".format(num1))


# Indicando un padding se pueden poner los ceros!
# Padding a 16 bits
print("{0:016b}".format(num1))

# Padding a 8 bits:
s ="{0:08b}".format(num1)
print(s, type(s))
