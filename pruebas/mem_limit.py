import random

@profile
def f(n):
	return [random.randint(100, 2000000) for i in range(n)]


for i in range(50):
	f(10000)
