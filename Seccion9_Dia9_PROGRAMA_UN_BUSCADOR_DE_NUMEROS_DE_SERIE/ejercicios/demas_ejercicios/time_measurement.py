import time

def prueba_for(numero):
    lista = []
    for num in range(1,numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    for num in range(1,numero+1):
        lista.append(num)
        contador+=1
    return lista

inicio1 = time.time()
prueba_for(10000)
final1 = time.time()


inicio2 = time.time()
prueba_while(10000)
final2 = time.time()

print(final1-inicio1) # El ciclo for es más rápido en esta prueba
print(final2-inicio2)

import timeit


declaracion ="""
prueba_for(10)
"""

mi_setup ="""
def prueba_for(numero):
    lista = []
    for num in range(1,numero+1):
        lista.append(num)
    return lista
"""

duracion = timeit.timeit(declaracion,mi_setup,number=1000000) # El ciclo for es más rápido en esta prueba
print(duracion)


declaracion2 ="""
prueba_while(10)
"""

mi_setup2 ="""
def prueba_while(numero):
    lista = []
    contador = 1
    for num in range(1,numero+1):
        lista.append(num)
        contador+=1
    return lista
"""

duracion2 = timeit.timeit(declaracion2,mi_setup2,number=1000000)
print(duracion2)