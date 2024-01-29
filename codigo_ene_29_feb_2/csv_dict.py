"""
Conversor de texto en CSV a dict.
"""

csv = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

def csvToDict(csv, sep=';'):
    # Devolver un dict por cada una de la filas.
    d = dict()
    filas = csv.split(r"\n")
    cabs = filas[0].split(";")
    filas[1:]

if __main__=='__main__':
    csvToDict(csv)

