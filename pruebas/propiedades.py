class Boletin:
	def __init__(self, *notas):
		self.notas = list(notas)

	@property
	def media(self):
		if len(self.notas):
			return sum(self.notas)/len(self.notas)
		return 0
		
	@property
	def ultima_nota(self):
		if len(self.notas):
			return self.notas[-1]
			
	@ultima_nota.setter
	def ultima_nota(self, nota):
		self.notas.append(nota)
		
	@ultima_nota.deleter
	def ultima_nota(self):
		self.notas.pop()

if __name__ == '__main__':
	
	b = Boletin(1,5,8,7,5)
	print(b.media)
	b.ultima_nota = 10
	print(b.media)
	del b.ultima_nota
	print(b.media)
	
	
