"""
POO en Python
"""

class Pedido:
    """
    Implementación de la clase Pedido
    """

    def __init__(self, idpedido=0, idcliente='', importe=0.0, pais=''):
        self.idpedido = idpedido
        self.idcliente = idcliente
        self.importe = importe
        self.pais = pais

    def __str__(self):
        return str(self.idpedido) + ' ' + self.idcliente + ' ' + str(self.importe) + ' ' + self.pais


if __name__ == '__main__':
    ped1 = Pedido(10440, 'ALFKI', 23.56, 'España')
    print(ped1)
    print(str(ped1))
    print(ped1.__str__())

