import base64, binascii


cadena = "hola mundo"
s = ":".join("{:02x}".format(ord(c)) for c in cadena)
print(s)

deadbeef = binascii.unhexlify('DEADBEEF')
print('DEADBEEF',deadbeef)

# Given raw bytes, get an ASCII string representing the hex values
hex_data = binascii.hexlify(b'\x00\xff')  # Two bytes values 0 and 255

# The resulting value will be an ASCII string but it will be a bytes type
# It may be necessary to decode it to a regular string
text_string = hex_data.decode('utf-8')  # Result is string "00ff"
print(text_string)

print('--------------------------')
a = base64.b64encode(b'cadena normal')
b = base64.b64decode(a)

print(a)
print(b)
print()

a = base64.b64encode(bytes('complex string: ñáéíóúÑ', "utf-8"))
b = base64.b64decode(a).decode("utf-8", "ignore")

print(a)
print(b)
