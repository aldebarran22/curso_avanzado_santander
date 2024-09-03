import sys
path = sys.argv[0] #'parametros_argv.py'
cadenas = path.split("/")
print(cadenas[-1])
fichero = "copia de "+cadenas[-1]
pathfinal = "/".join(cadenas[:-1])+"/"+fichero
print(pathfinal)

'''
pos = path.rindex('.')

fich = None

try:
    fich = open(path, "r")
    while True:
        linea = fich.readline()
        if not linea:
            break
        print(linea.strip())

except Exception as e:
    print(e)

finally:
    if fich:
        fich.close()

'''
