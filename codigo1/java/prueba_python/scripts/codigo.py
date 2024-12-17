"""
Escribe informacion en un fichero de texto
"""

fich = open("informacion.txt", "w")
fich.write("Contenido del fichero\n")
fich.write("Contenido del fichero 2\n")
fich.write("Contenido del fichero 3\n")
fich.close()