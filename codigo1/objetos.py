"""
POO en Python
"""
def crearObjeto(clase, *args):
    return clase(*args)

class Pedido:
    """
    Implementación de la clase pedido
    """

    def __init__(self, idpedido=0, cliente='', importe=0.0, pais=''):
        self.idpedido = idpedido
        self.cliente = cliente
        self.importe = importe
        self.pais = pais

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.idpedido) + " " + self.cliente + " " + str(self.importe) + " " + self.pais

if __name__ == '__main__':
    pedido = Pedido(10248, 'ALFKI', 34.99, "España")
    print(pedido)
    #print(str(pedido))
    #print(pedido.__str__())
    pedido.iva = 3.44
    pedido.__dict__['dto'] = 1.5
    print(pedido.__dict__)
    print("La clase: ",pedido.__class__.__name__)

    pedido2 = crearObjeto(Pedido, 10250, 'FRTEE', 23.8, "Francia")
    print(pedido2)

    pedido3 = crearObjeto(pedido.__class__, 10260, 'FGHAE', 113.9, "Alemania")
    print(pedido3)

    L = [pedido, pedido2, pedido3]
    print(L)
    L.sort(key=lambda ped : ped.importe, reverse=True)
    print(L)
