
from i18n import Singletoni18n

def funcion1():
    print(Singletoni18n.getInstance("es")['twitter'])
    print(Singletoni18n.getInstance("en")['twitter'])


if __name__ == '__main__':
    print(Singletoni18n.getInstance("es")['inicio'])
    print(Singletoni18n.getInstance("es")['facebook'])
