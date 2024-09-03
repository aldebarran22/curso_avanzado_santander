from pysimplesoap.client import SoapClient, SoapFault

try:
    cliente = SoapClient(
        location="http://localhost:8008/",
        action="http://localhost:8008/",
        namespace="http://example.com/sample.wsld",
        soap_ns="soap",
        ns="ns",
    )

    response = cliente.Hello(name="World")
    print("Respuesta server: ", response.mensaje)

    response2 = cliente.Operar(num1=10, num2=20, op="sum")
    print("Respuesta server: ", response2.resul)

except Exception as e:
    print(e.__class__.__name__, e)
