# Acceso a elementos de una lista con un bucle for

nombres = ["Ana", "Juan", "Pedro", "María"]

for nombre in nombres:
    print(nombre)

numeros = [[1, 2], [3, 4], [5, 6]]

for a, b in numeros:
    print(f"Posición 0: {a}, Posición 1: {b}")


# Acceso a elementos de un diccionario con un bucle for

diccionario = {"a": 1, "b": 2, "c": 3}


for item in diccionario:
    print(f"Clave: {item}, Valor: {diccionario[item]}")

for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")