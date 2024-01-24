from collections import namedtuple

Punto = namedtuple('Punto', ['x','y'])
p = Punto(8,9)
print(p)

print(p.x)
print(p.y)

print(Punto.__class__)
