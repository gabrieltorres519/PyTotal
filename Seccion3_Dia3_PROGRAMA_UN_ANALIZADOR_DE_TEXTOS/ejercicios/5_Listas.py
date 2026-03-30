# Sección Listas

# Una lista es una secuencia ordenada de elementos que pueden ser de diferentes tipos de datos.
# Las listas son mutables, lo que significa que sus elementos pueden ser modificados después de su creación.
# Se pueden anidar listas dentro de otras listas para crear estructuras de datos más complejas.
# Al igual de los strings, podemos indexarlas y fraccionarlas.


mi_lista = ['a', 'b', 'c', 'd', 'e']
print(type(mi_lista))  # <class 'list'>
print(mi_lista)        # ['a', 'b', 'c', 'd', 'e']

lista_variada = [1, 'hola', 3.14, True, [1, 2, 3]]
print(lista_variada)  # [1, 'hola', 3.14, True, [1, 2, 3]]

# Longitud de la lista
print(len(mi_lista))  # 5
# Acceso a elementos
print(mi_lista[0])    # 'a'
print(mi_lista[-1])   # 'e'
# Modificación de elementos
mi_lista[1] = 'z'
print(mi_lista)       # ['a', 'z', 'c', 'd', 'e']
# Agregar elementos
mi_lista.append('f')
print(mi_lista)       # ['a', 'z', 'c', 'd', 'e', 'f']
# Eliminar elementos
mi_lista.remove('c')
print(mi_lista)       # ['a', 'z', 'd', 'e', 'f']
# Anidación de listas
lista_anidada = [1, 2, [3, 4], 5]
print(lista_anidada[2])      # [3, 4]
print(lista_anidada[2][0])   # 3    # Accesando al primer elemento de la lista anidada

# Rangos y fraccionamiento
print(mi_lista[1:4])  # ['z', 'd', 'e'] 
print(mi_lista[:3])   # ['a', 'z', 'd'] siendo equivalente a mi_lista[0:3]
print(mi_lista[2:])   # ['d', 'e', 'f'] siendo equivalente a mi_lista[2:len(mi_lista)]

# Concatenación de listas al mostrarlas en pantalla
otra_lista = ['x', 'y', 'z']
print(mi_lista + otra_lista)  # ['a', 'z', 'd', 'e', 'f', 'x', 'y', 'z']

# Concatenar usando una nueva lista
nueva_lista = mi_lista + otra_lista
print(nueva_lista)  # ['a', 'z', 'd', 'e', 'f', 'x', 'y', 'z']


# Eliminar el último elemento de una lista
ultimo_elemento = mi_lista.pop()
print(ultimo_elemento)  # 'f'
print(mi_lista)         # ['a', 'z', 'd', 'e']

# El método sort() ordena la lista en su lugar baseado en el orden natural de los elementos, como números o letras.
# El método sort() no devuelve una nueva lista, sino que modifica la lista original. Si lo intentamos tendremos un objeto de tipo Nonetype (el resultado de un método que no devuelve nada).
# Si queremos crear una nueva lista ordenada sin modificar la original, podemos usar la función sorted().
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print(numeros)  # [1, 2, 5, 5, 6, 9]

# Después de ordenar una lista, podemos invertir su orden usando el método reverse().
numeros.reverse()
print(numeros)  # [9, 6, 5, 5, 2, 1]







# Sección metodo flech kincaid

import re

def flesch_kincaid2(text): 

    print(text)
    
    palabras_totales = 0

    sentences = text.split(".")
    sentences = re.split(r'[.!?]+', text)
    # sentences = text
    silabas = 0

    print(f'Oraciones totales: {sentences}')

    for sentence in sentences:


        # Si sentence es un array vacio, restamos 1 a oraciones totales
        if sentence == "":
            print("oracion vacia")
            oraciones_totales = len(sentences) - 1
            print("Oraciones totales ajustadas: " + str(oraciones_totales))
            continue


        palabras = sentence.split(" ")

        if "" in palabras:
            print("entro")
            position = palabras.index("")
            palabras.pop(position)

        palabras_totales = palabras_totales + (len(palabras))
        print("Palabras en la oracion actual: " + str(len(palabras)))
        print(palabras)


        for palabra in palabras:

            contador = 0

            for letra in palabra:

                if len(palabra) > 2 and (contador + 1) <= len(palabra):

                    if contador > 0 and contador < len(palabra) - 1:

                        if letra in "aeiouAEIOU" and (palabra[contador - 1] not in "aeiouAEIOU"):
                            silabas = silabas + 1

                    elif contador == len(palabra) - 1:

                        if letra in "aeiouAEIOU" and (palabra[contador - 1] not in "aeiouAEIOU"):
                            silabas = silabas + 1

                    elif contador == 0:

                        if letra in "aeiouAEIOU":
                            silabas = silabas + 1

                elif len(palabra) == 1:
                    if letra in "aeiouAEIOU":
                        silabas = silabas + 1

                elif len(palabra) == 2:
                    
                        if letra in "aeiouAEIOU":
                            silabas = silabas + 1
            
                contador = contador + 1
                

    
    
    print("Palabras totales " + str(palabras_totales))
    print("Oraciones totales " + str(oraciones_totales))
  

    average_words_per_sentence = palabras_totales / oraciones_totales
    print("Promedio de palabras por oración:", average_words_per_sentence)
    print("Numero de silabas en el texto:", silabas)

    array = [1,2,3,4]
    print(array[1:4])   

    average_syllables_per_word = silabas / palabras_totales
    print("Promedio de silabas por palabra:", average_syllables_per_word)  

    # (0.39 * average number of words per sentence) + (11.8 * average number of syllables per word) - 15.59
    fk_score = (0.39 * average_words_per_sentence) + (11.8 * average_syllables_per_word) - 15.59
    print("Flesch-Kincaid score:", fk_score)

    return fk_score

text = input("Ingresa el texto largo: ")


flesch_kincaid2(text) 