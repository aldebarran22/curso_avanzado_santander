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


def csvToDict(csv, sep=";"):
    # Devolver un dict por cada una de la filas.
    filas = csv.split("\n")
    cabs = filas[0].split(sep)
    return [dict(zip(cabs, i.split(sep))) for i in filas[1:]]


def dictToCSV(L, sep=";"):
    # Devolver un bloque de texto en formato CSV:
    cabs = sep.join(L[0].keys())
    lineas = [sep.join(i.values()) for i in L]
    lineas.insert(0, cabs)
    return "\n".join(lineas)


def dictToCSV2(L, sep=";"):
    # Devolver un bloque de texto en formato CSV:
    cabs = sep.join(L[0].keys())
    lineas = [sep.join(i.values()) for i in L]
    lineas.insert(0, cabs)
    return "\n".join(lineas)


if __name__ == "__main__":
    L = csvToDict(csv)
    for i in L:
        print(i)
    txt = dictToCSV(L)
    print(txt)
    print(txt == csv)


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


def csvToDict(csv, sep=";"):
    # Devolver un dict por cada una de la filas.
    filas = csv.split("\n")
    cabs = filas[0].split(sep)
    return [dict(zip(cabs, i.split(sep))) for i in filas[1:]]


def dictToCSV(L, sep=";"):
    # Devolver un bloque de texto en formato CSV:
    cabs = sep.join(L[0].keys())
    lineas = [sep.join(i.values()) for i in L]
    lineas.insert(0, cabs)
    return "\n".join(lineas)


def dictToCSV2(L, sep=";"):
    # Devolver un bloque de texto en formato CSV:
    cabs = sep.join(L[0].keys())
    lineas = [sep.join(i.values()) for i in L]
    lineas.insert(0, cabs)
    return "\n".join(lineas)


if __name__ == "__main__":
    L = csvToDict(csv)
    for i in L:
        print(i)
    txt = dictToCSV(L)
    print(txt)
    print(txt == csv)
