from collections import Counter, defaultdict, namedtuple

# el módulo collections nos ofrece varias estructuras de datos que facilitan el trabajo con colecciones de datos, como listas, diccionarios, tuplas, etc.
# principalmente para contar elementos, manejar diccionarios con valores por defecto, crear tuplas con nombres, etc.

"""El objeto Counter nos facilita el proceso de conteo de apariciones de un elemento en una lista o string"""
numeros = [5,6,4,3,9,0,1,2,4,3]
print(Counter(numeros))
print(Counter('Missisipi'))

"""Se puede aplicar con palabras en un string"""
frase = 'El pan al pan y el vino al vino'
print(Counter(frase.split()))

"""Adicionalmente Counter devuelve un objeto (todo en python es un objeto) que tiene métodos que podemos usar"""
serie = Counter([5,6,4,3,9,0,1,2,4,3])
print(serie.most_common(1))  # Se pasa como argumento 1 si solo se quiere el que más se repite, 3 para el top 3, etc.

"""Podemos también obtener los elementos únicos de la lista, sin sus repeticiones"""
serie = Counter([5,6,4,3,9,0,1,2,4,3])
print(list(serie))

"""
Hablando del objeto defaultdict, este sirve para iterar en diccionarios que pueden no contener claves que bucasmos
para evitar que se lanze un error
"""
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
#print(mi_diccionario['d'])  # Esto lanzará un error porque la clave 'd

mi_diccionario = defaultdict(int)  # Se le puede pasar un tipo de dato para que lo use como valor por defecto

mi_diccionario['a'] = 1

print(mi_diccionario['d'])  # Esto no lanzará un error, sino que devolverá el valor por defecto que es 0 en este caso, 
                            # porque se le pasó int como tipo

"""Un segundo ejemplo con una función lambda para devolver un string por defecto"""
mi_diccionario = defaultdict(lambda: "Valor por defecto")
mi_diccionario['a'] = "Valor para clave 'a'"
print(mi_diccionario['a'])  # Devolverá "Valor para clave 'a'"
print(mi_diccionario['d'])  # Devolverá "Valor por defecto"


"""
Igualmente se puede dar el trabajo con tuplas, para que en lugar de acceder a los elementos por su posición, 
lo hagamos con un nombre
"""
mi_tupla = (500,18,65)

print(mi_tupla[1]) # Devolverá el 18

Persona = namedtuple('Persona', ['nombre','altura','peso'])
ariel = Persona('Ariel', 1.76, 79)

print(ariel.altura)

"""Lista de ciudades con deque, que es una estructura de datos que permite agregar y eliminar elementos de ambos extremos de la lista,"""
from collections import deque 

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])