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

    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.importe < other.importe

class PedidoElectronico(Pedido):

    def __init__(self, idpedido=0, idcliente='', importe=0.0, pais='', certificado=False, email=''):
        Pedido.__init__(self, idpedido, idcliente, importe, pais) 
        # super(idpedido, idcliente, importe, pais)           
        self.certificado = certificado
        self.email = email

def pruebaPedidoElectronico():
    ped1 = PedidoElectronico(10440, 'ALFKI', 23.56, 'España', True, 'correo@gmail.com')
    print(ped1)

def pruebaPedido():
    ped1 = Pedido(10440, 'ALFKI', 23.56, 'España')
    print(ped1)
    #print(str(ped1))
    #print(ped1.__str__())
    ped2 = Pedido(10445, 'DEFRE', 123.02, 'Francia')
    ped4 = Pedido(10445, 'DEFRE', 123.02, 'Francia')
    ped3 = Pedido(11047, 'OLIKU', 85.44, 'Alemania')
    L = [ped1, ped2, ped3]
    print(L)
    L.sort(key=lambda obj : obj.pais)
    print(L)
    L.sort()
    if ped4 == ped2:
        print('ped4 == ped2')
    else:
        print('ped4 != ped2')

    ped1.iva = 2.44
    ped1.__dict__['dto'] = 0.78
    print(ped1.__dict__)
    print(ped1.__class__.__name__)

    obj = ped1.__class__(10099)
    print(obj)
    print(ped1.__class__, Pedido)

if __name__ == '__main__':
    # pruebaPedido()
    pruebaPedidoElectronico()
