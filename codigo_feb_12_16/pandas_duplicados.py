import pandas as pd
from pandas import Series, DataFrame

datos = DataFrame({'k1':['one']*3 + ['two'] * 4,
				  'k2':[1,1,2,3,3,4,4]})
print('\n',datos)

#mostrar los duplicados:
print('\n',datos.duplicated())

datos2 = datos.drop_duplicates()
print('\n',datos2)				  
