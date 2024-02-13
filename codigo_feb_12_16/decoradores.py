AUTHENTICATED = False


def autenticado(f):
    def inner(*args, **kwargs):
        print("Yo autentico")
        if AUTHENTICATED:
            print("Voy a llamar a ", f.__name__)
            f(*args, **kwargs)  # Aqui es donde se ejecuta la funcion abrirPuerta
            print("args", args)
            print("kwargs", kwargs)

        else:
            raise Exception("No tiene permisos de ejecución")

    return inner


def aviso(f):
    def inner(*args, **kwargs):
        print("Yo aviso")
        f(*args, **kwargs)
        print("Se ejecuto %s" % f.__name__)

    return inner


@autenticado
def abrir_puerta(a, b, c, L, *args, **kwargs):
    print("en abrir puerta")
    print("a,b,c,L", a, b, c, L)
    print("opcionales tupla:", args)
    print("opcionales dict:", kwargs)
    print("Abrir la puerta")


@autenticado
def cerrar_puerta():
    print("Cerrar la puerta")


# Programa principal:
try:
    abrir_puerta(1, 2, 3, list(range(5)), 3, 4, p1=0, p2=1)
    # cerrar_puerta()
except Exception as e:
    print("Error:", e)
