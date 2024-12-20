"""
Enviar contenido a consola, a un fichero.
"""
import sys

def imprimir(texto, file=sys.stdout):
    print(texto, file=file)


if __name__ == '__main__':
    fich = open("salida.txt", "w")
    imprimir("Este mensaje va a consola")
    imprimir("Este mensaje va a fichero", fich)
    fich.close()

