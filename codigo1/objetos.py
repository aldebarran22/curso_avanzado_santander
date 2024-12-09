"""
POO en Python
"""

class Pedido:
    """
    Implementación de la clase pedido
    """

    def __init__(self, idpedido=0, cliente='', importe=0.0, pais=''):
        self.idpedido = idpedido
        self.cliente = cliente
        self.importe = importe
        self.pais = pais

    def __str__(self):
        return str(self.idpedido) + " " + self.cliente + " " + str(self.importe) + " " + self.pais

if __name__ == '__main__':
    pedido = Pedido(10248, 'ALFKI', 34.99, "España")
    print(pedido)

