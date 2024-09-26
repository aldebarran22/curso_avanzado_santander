
from datetime import datetime
from time import strftime

fich = open("scripts/contenido.txt", "w")
t = datetime.now()
fich.write("mensaje generado a las: "+ t.strftime("%d/%m/%Y %H:%M"))
fich.close()
