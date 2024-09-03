import random

fich="numeros.bin"
f = open(fich, "wb")
LEscritura=[]
n=10
for i in range(n):
    valor = random.randint(1,1000)
    LEscritura+=[valor]
    valorEnBytes = valor.to_bytes(2,byteorder='little',signed=False)
    print("%d %X" % (valor,valor), end=" ")
    print(valorEnBytes)
    f.write(valorEnBytes)
f.close()


f=open(fich, "rb")
LLectura=[]
i = 0
for i in range(n):
    datoEnBytes = f.read(2)

    dato = int.from_bytes(datoEnBytes,byteorder='little',signed=False)
    LLectura+=[dato]

    print(dato, hex(dato))

f.close()

if LEscritura==LLectura:
    print("Iguales")
else:
    print("No iguales")
