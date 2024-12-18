"""
Generar formatos:
json
xml: DOM / SAX / XPath
Serialización:
- Pickle
- Shelve
"""

from base_datos import Categoria, Producto, BaseDatos
import json

def exportarJson(L, path):
    """Exportar todos los productos con la categoría a un fichero json"""
    fich = None
    try:
        fich = open(path, 'w')
        R = [objeto.to_json() for objeto in L]
        json.dump(R, fich, indent=4)
        print(f'Se ha generado el fichero: {path}')
        
    except Exception as e:
        raise e
    
    finally:
        if fich:fich.close()

if __name__ == '__main__':
    try:
        bd = BaseDatos("empresa3.db")
        L = bd.select()
        exportarJson(L, "productos.json")

    except Exception as e:
        print(e)
    
