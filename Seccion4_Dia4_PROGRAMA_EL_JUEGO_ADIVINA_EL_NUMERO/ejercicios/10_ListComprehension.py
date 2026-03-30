palabra = "python"

# Podemos generar una lista con cada uno de los elementos del string

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)
# ['p', 'y', 't', 'h', 'o', 'n']

# Esto se puede hacer con una sola línea de código utilizando List Comprehension
letras = [letra for letra in palabra]   
print(letras)
# ['p', 'y', 't', 'h', 'o', 'n']

numeros = [n for n in range(10)]
print(numeros)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mitades = [n/2 for n in range(10)]
print(mitades)
# [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]


# Condicionar qué elementos se añaden a la lista
pares = [n for n in range(10) if n % 2 == 0]
print(pares)
# [0, 2, 4, 6, 8]

# Una selección más compleja
lista = [n if n * 2 > 10 else 'no' for n in range(10)]
print(lista)
# ['no', 'no', 'no', 'no', 'no', 6, 8, 10, 12, 14]

pies = [10, 20, 30, 40, 50]
metros = [pie * 0.3048 for pie in pies]
print(metros)
# [3.048, 6.096, 9.144, 12.192, 15.24]


