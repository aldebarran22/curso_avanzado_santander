"""
Exportar a JSON / XML empleados de la BD
"""

from basedatosCRUD import BaseDatos
import json

def exportarJSON(bd, path):
    fich = None
    try:
        fich = open(path, "w")
        empleados = bd.select()
        L = [emp.__dict__ for emp in empleados]
        json.dump(L, fich, indent=4)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    bd = BaseDatos("../BBDD/empresa3.db")
    exportarJSON(bd, "ficheros/empleados.json")
