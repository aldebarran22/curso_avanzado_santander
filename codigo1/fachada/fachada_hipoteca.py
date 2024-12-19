class SistemaDeCreditos(object):
	
	def comprobarSiHayCreditos(self, cliente):
		print("Comprobando cliente en el sistema de creditos")
		return True
		
		
class SistemaMorosidad(object):
	
	def comprobarImpagos(self, cliente):
		print("Comprobando cliente en el sistema de Morosidad")
		return True		

class Cliente(object):
	
	def __init__(self, dni, nombre, saldo):
		self.dni = dni
		self.nombre = nombre
		self.saldo = saldo
		
class Banco(object):
		
	def comprobarCuentaCliente(self, cliente, cantidad):
		print("El banco comprueba el saldo del cliente")
		return True

class Fachada(object):
	
	def __init__(self, banco, sm, sc):
		self.banco = banco
		self.sm = sm
		self.sc = sc
		
	def concederHipoteca(self, cliente, valorHipoteca):
		if not banco.comprobarCuentaCliente(cliente, valorHipoteca):
			print("Rechazo de la hipoteca por el banco")
			return False

		if not sm.comprobarImpagos(cliente):
			print("Rechazo de la hipoteca por morosidad")
			return False
					
		if not sc.comprobarSiHayCreditos(cliente):
			print("Rechazo de la Hipoteca por el sistema de creditos") 
			return False
		
		return True
			
if __name__=="__main__":
		cli = Cliente("615252524S","Ana Gomez", 36000)
		banco = Banco()
		sm = SistemaMorosidad()
		sc = SistemaDeCreditos()
		
		cantidad = 240000
		fachada = Fachada(banco, sm, sc)
		
		if fachada.concederHipoteca(cli, cantidad):
			print("Se concede la hipoteca de",cantidad)
		
		else:
			print("NO se concede la hipoteca")
