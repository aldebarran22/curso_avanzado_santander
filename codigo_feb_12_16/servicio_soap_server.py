from pysimplesoap.server import SoapDispatcher, SOAPHandler
from http.server import HTTPServer

def hello(name):
    # Esta es la funcionalidad para publicar con el WS
    return {'mensaje':'hello %s' % name}

def operacion(num1, num2, op):
    if op == "sum":
        return {'resul': 'suma:'+str((num1+num2))}

    elif op == 'sub':
        return {'resul': 'resta:'+str((num1-num2))}

    else:
        return {'resul':'operacion no existe'}

# Crear el dispatcher
dispatcher = SoapDispatcher('mi_dispatcher', location='http://localhost:8008/', \
action = 'http://localhost:8008/', namespace = 'http://example.com/sample.wsdl', \
    prefix='ns0', trace=True, ns = True)

dispatcher.register_function('Hello', hello, returns={'mensaje':str}, args={'name':str})
dispatcher.register_function('Operar', operacion, returns={'resul':str}, args={'num1':int, 'num2':int, 'op':str})
if __name__ == '__main__':
    server = HTTPServer(("", 8008), SOAPHandler)
    server.dispatcher = dispatcher
    print('Servidor on en el puerto 8008')
    server.serve_forever()