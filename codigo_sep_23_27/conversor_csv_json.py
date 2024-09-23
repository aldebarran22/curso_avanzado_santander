"""Convertir texto en CSV a json"""

csv="""id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

def tojson(formato_csv, sep=';'):
    L = formato_csv.split("\n")
    cabs = L[0].split(sep)
    resul = []
    for i in L[1:]:
        datos = i.split(sep)
        d = dict(zip(cabs, datos))
        resul.append(d)
    return resul

def tocsv(formato_json, sep=';'):
    cabs = sep.join(formato_json[0].keys())
    L = [cabs]
    for i in formato_json:
        L.append(sep.join(i.values()))
    return "\n".join(L)

if __name__ == '__main__':
    d = tojson(csv)
    csv2 = tocsv(d)
    print(csv == csv2)