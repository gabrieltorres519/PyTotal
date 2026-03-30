from random import *

# Los métodos más usados del módulo random son:
# random(): Devuelve un número decimal aleatorio entre 0.0 y 1.0.
# randint(a, b): Devuelve un número entero aleatorio entre a y b (ambos inclusive).
# choice(seq): Devuelve un elemento aleatorio de una secuencia no vacía
# shuffle(x): Mezcla aleatoriamente los elementos de la lista x in situ.
# uniform(a, b): Devuelve un número decimal aleatorio entre a y b.
 
aleatorio_entero = randint(1,50) # Devuelve un número entero aleatorio entre 1 y 50 (ambos inclusive).
print("Número aleatorio entre 1 y 50:", aleatorio_entero)

aleatorio_decimal = round(uniform(1,5),1) # Devuelve un número decimal aleatorio entre 1 y 5, redondeado a 1 decimal.
print("Número decimal aleatorio entre 1 y 5:", aleatorio_decimal)

opciones = ["piedra", "papel", "tijeras"]
eleccion_aleatoria = choice(opciones) # Devuelve un elemento aleatorio de la lista opciones.
print("Elección aleatoria entre piedra, papel y tijeras:", eleccion_aleatoria)


numeros = [1, 2, 3, 4, 5]
shuffle(numeros) # Mezcla aleatoriamente los elementos de la lista numeros in situ
print("Lista de números mezclada aleatoriamente:", numeros)

