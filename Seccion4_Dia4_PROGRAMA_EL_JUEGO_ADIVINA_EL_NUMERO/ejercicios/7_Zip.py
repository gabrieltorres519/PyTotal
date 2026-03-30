# El método zip() se utiliza para combinar dos o más iterables (como listas, tuplas, etc.) 
# en un solo iterable de tuplas. Cada tupla contiene elementos correspondientes de los iterables originales.

lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
combinada = zip(lista1, lista2)
print(list(combinada))  # Convertimos el resultado a una lista para mostrarlo

# Como se puede observar, las listas deben de ser del mismo tamaño, de lo contrario, zip() solo combinará 
# hasta el tamaño del iterable más corto.
lista3 = ['x', 'y']
combinada2 = zip(lista1, lista3)
print(list(combinada2))  # Solo combina hasta el tamaño de lista3

# Notar que zip() no se utiliza solo, tambien requiere el tipo de objeto al que se le va a convertir, como list(), tuple(), etc.

