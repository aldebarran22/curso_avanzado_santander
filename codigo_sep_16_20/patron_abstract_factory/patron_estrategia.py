

def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoBurbuja(unaLista)
print(unaLista)

###############################################################################################
def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual

unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoPorInsercion(unaLista)
print(unaLista)