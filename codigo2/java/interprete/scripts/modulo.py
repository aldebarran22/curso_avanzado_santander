from datetime import datetime

fich = open("scripts/informacion.txt", "w")
t = datetime.now()
cad = t.strftime("%d/%m/%Y, %H:%M:%S")
linea = "Fichero generado a las "+cad
fich.write(linea)
fich.close()
