"""
Generar un histograma con la clase Counter
"""

from collections import Counter

cad = "mississippi"
c = Counter(cad)
print(c)
dic = dict(c)
print(dic)
print(list(dic.items()))
