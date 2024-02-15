"""
Exportar a JSON / XML empleados de la BD
"""

from basedatosCRUD import BaseDatos, Empleado
import json
from xml.etree.ElementTree import Element, SubElement, tostring, Comment
from xml.etree import ElementTree


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


def exportarXML(bd, path):
    top = Element("empleados")
    empleados = bd.select()
    for e in empleados:
        empleado = SubElement(top, "empleado", {"id":str(e.id)})
        nombre = SubElement(empleado, "nombre")
        nombre.text = e.nombre
        cargo = SubElement(empleado, "cargo")
        cargo.text = e.cargo
    print(tostring(top))


if __name__ == "__main__":
    bd = BaseDatos("../BBDD/empresa3.db")
    # exportarJSON(bd, "ficheros/empleados.json")
    # L = importarJSON("ficheros/empleados.json")
    # print(L[:3])
    exportarXML(bd, "ficheros/empleados.xml")
