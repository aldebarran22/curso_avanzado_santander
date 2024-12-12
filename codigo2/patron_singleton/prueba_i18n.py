
from i18n import Singletoni18n
from prueba2_i18n import funcion3

def funcion1():
    print(Singletoni18n.getInstance("es")['twitter'])
    print(Singletoni18n.getInstance("en")['twitter'])


if __name__ == '__main__':
    print(Singletoni18n.getInstance("es")['inicio'])
    print(Singletoni18n.getInstance("es")['facebook'])
    funcion1()
    funcion3()