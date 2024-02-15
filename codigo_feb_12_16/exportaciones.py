"""
Exportar a JSON / XML empleados de la BD
"""

from basedatosCRUD import BaseDatos, Empleado
import json


def exportarJSON(bd, path):
    fich = None
    try:
        fich = open(path, "w")
        empleados = bd.select()
        L = [emp.__dict__ for emp in empleados]
        json.dump(L, fich, indent=4)
        # print(json.dumps(L, indent=4)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def importarJSON(path):
    fich = None
    try:
        fich = open(path, "r")
        # Restaurar una lista de dict de Python
        L = json.load(fich)
        # Pasar de la lista de dict a una lista de objetos Empleado
        empleados = [Empleado(**d) for d in L]
        return empleados

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    bd = BaseDatos("../BBDD/empresa3.db")
    exportarJSON(bd, "ficheros/empleados.json")
    L = importarJSON("ficheros/empleados.json")
    print(L[:3])
