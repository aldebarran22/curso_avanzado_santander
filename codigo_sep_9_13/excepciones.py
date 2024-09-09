"""
Obtener el nombre de la clase de la excepcion
"""

def get(i):
    L = [1,2,3,4,5]
    return L[i] # lanza IndexError


if __name__ == '__main__':
    try:
        i = 10
        i()
        resul = get(10)
    except Exception as e:
        print(e.__class__.__name__, e)