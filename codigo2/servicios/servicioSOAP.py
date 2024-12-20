"""
Implementación de un Servicio SOAP con la librería pysimplesoap
"""

from pysimplesoap.server import SoapDispatcher, SOAPHandler
from http.server import HTTPServer


def hello(name):
    return {"mensaje": f"Hello {name}"}


# Crear el dispatcher:
dispatcher = SoapDispatcher(
    "mi_dispatcher",
    location="http://localhost:8008/",
    action="http://localhost:8008/",
    namespace="http://example.com/sample.wsdl",
    prefix="ns0",
    trace=True,
    ns=True,
)

# Registrar la función
dispatcher.register_function(
    "Hello", hello, returns={"mensaje": str}, args={"name": str}
)

# Poner en marcha el servidor:
if __name__ == "__main__":
    print("Servidor Ok!")
    server = HTTPServer(("", 8008), SOAPHandler)
    server.dispatcher = dispatcher
    server.serve_forever()
