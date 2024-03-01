from pysimplesoap.client import SoapClient, SoapFault

try:
	cliente = SoapClient(location='http://localhost:8008/',
	action = 'http://localhost:8008/',
	namespace = 'http://example.com/sample.wsld',
	soap_ns = 'soap',
	ns = 'ns')
	
	response = cliente.Hello(name='World')
	print('Respuesta server: ', response.mensaje)
	
except Exception as e:
	print(e.__class__.__name__, e)
