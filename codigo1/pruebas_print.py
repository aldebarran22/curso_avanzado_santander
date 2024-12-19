"""
Mostrar texto en columnas
"""

L = [{"nombre":"Ana", "edad":4,"altura":1.7},
     {"nombre":"Jose", "edad":24,"altura":1.67},
     {"nombre":"Jose Antonio", "edad":54,"altura":1.885}]
cabs = tuple(L[0].keys())
for d in L:
    t = tuple(d.values())
    print("%-15s\t%2d\t%.2f" % t)
   