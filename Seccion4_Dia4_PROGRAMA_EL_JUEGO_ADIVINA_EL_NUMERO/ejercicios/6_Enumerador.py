lista = ['a', 'b', 'c', 'd', 'e']

for item in enumerate(lista):
    print(item)

for index, item in enumerate(lista):
    print(f'El índice es: {index} y el valor es: {item}')

# Enumerate tambien se puede usar con strings, integers en un rango, etc.

# convertir una lista en formato tupla 
lista_tupla = list(enumerate(lista))
print(lista_tupla)

def array_diff(a, b):
    for item in b:
        if item in a:
            times_it_repeats = a.count(item)
            for i in range(times_it_repeats):
                index_necessary = a.index(item)
                a.pop(index_necessary)
        else:
            continue
    return a

print(array_diff([1, 2, 2], [2]))

def array_diff2(a, b):
    return [x for x in a if x not in b] # Retorna x para cada x en a, si x no está en b. 
    # Esta expresion se llama "list comprehension", es una forma más eficiente de escribir código que genera una lista a partir de otra lista.

print(array_diff2([1, 2, 2], [2]))