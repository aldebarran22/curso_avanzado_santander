"""
Exportar a JSON / XML empleados de la BD
"""

from basedatosCRUD import BaseDatos


def exportarJSON(bd, path):
    pass


if __name__ == "__main__":
    bd = BaseDatos("../BBDD/empresa3.db")
    exportarJSON(bd, "ficheros/empleados.json")
