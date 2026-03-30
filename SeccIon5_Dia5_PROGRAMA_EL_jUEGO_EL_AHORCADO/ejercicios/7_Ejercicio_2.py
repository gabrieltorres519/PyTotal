def funcion(palabra):
    
    palabra = list(palabra)

    for letra in palabra:

        repeticiones = palabra.count(letra)

        if repeticiones > 1:
            for i in range(repeticiones-1):
                indice = palabra.index(letra)
                palabra.pop(indice)
                print('borrado')
        repeticiones -= 1
                        
    CadenaFinal = sorted(palabra)

    return ''.join(CadenaFinal)

print(funcion('dabfgzyyyyr'))

# Para eliminar elementos repetidos y que no haya restricción de solo usar listas se pueden usar
# sets, los cuales no permiten elementos repetidos

def funcion2(palabra):

    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)
    
    mi_lista = list(mi_set)
    mi_lista.sort()

    return ''.join(mi_lista)

print(funcion2('dabfgzyyyyr'))
