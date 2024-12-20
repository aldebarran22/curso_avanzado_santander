"""
Generar columnas alineadas con la función print y una cadena formato
"""

L = [{"producto":"HP", "precio":450.8, "uds":23},
     {"producto":"Sobremesa", "precio":1650.0, "uds":2},
     {"producto":"Portátil", "precio":854.81, "uds":120}]

print("%-15s\t%8s\t%8s" % ("PRODUCTO","PRECIO","UNIDADES"))
for d in L:
    print("%-15s\t%8.2f\t%8d" % (d['producto'], d['precio'], d['uds']))