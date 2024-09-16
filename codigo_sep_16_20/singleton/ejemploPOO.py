# -*- coding: cp1252 -*-
import time

class Singleton:

    __instance = None

    @staticmethod
    def getInstance(refresh = False):
        if Singleton.__instance == None or refresh:
            # Se crea el singleton
            Singleton.__instance = str(time.strftime("%H:%M:%S"))
                    
        return Singleton.__instance
            

print("Sin refresco, siempre la misma hora")    
print(Singleton.getInstance())
time.sleep(1)
print("siguiente llamada")
print(Singleton.getInstance())
print()

print("Con refresco, cada llamada cambia la hora")
print(Singleton.getInstance(True))
time.sleep(1)
print(Singleton.getInstance(True))



