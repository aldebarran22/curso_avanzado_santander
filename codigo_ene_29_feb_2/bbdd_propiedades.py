import sqlite3 as dbapi

print(dbapi.apilevel)

# De 0 a 3:
# 0: No se comparte (sincronización)
# 1: Se comparte el módulo pero no conexiones
# 2: Se comparten conexiones pero no cursores
# 3: Todo: módulo, cursores y conexiones.
print(dbapi.threadsafety)
print(dbapi.paramstyle)
