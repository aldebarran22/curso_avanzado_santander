# Prueba de un fichero de python para ejecutar desde Java

from datetime import datetime


fecha = datetime.now()
linea = "Texto generado a las: " + fecha.strftime("%d/%m/%Y %H:%M:%S")
fich = open("info.log", "w")
fich.write(linea)
fich.close()