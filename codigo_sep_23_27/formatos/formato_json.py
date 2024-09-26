"""
Carga de un fichero en Json
"""
import json

def cargaFich(path):
    fich = None
    try:
        fich = open(path, "r")
        objeto = json.load(fich)
        return objeto
    
    except Exception as e:
        print(e)

    finally:
        if fich: fich.close()

if __name__ == '__main__':
    lista = cargaFich("Pedidos.json")
    print(len(lista), "pedidos")
    print(lista[:2])
