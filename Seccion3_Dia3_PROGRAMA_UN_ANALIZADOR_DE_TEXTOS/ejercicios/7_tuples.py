# Muy similar a las listas o arrays, pero con la diferencia de que son inmutables.
# Una vez que un elemento fue asignado a una tupla, no puede ser modificado.

# Tienen dos formas de escribirse:
# 1. Con paréntesis
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# 2. Sin paréntesis
otra_tupla = 6, 7, 8, 9, 10
print(otra_tupla)
print(type(otra_tupla))

# Aun siendo más limitados que las listas, las tuplas tienen sus ventajas:
# 1. Son más rápidas que las listas.
# 2. Pueden ser usadas como claves en diccionarios (las listas no pueden).
# 3. Al ser inmutables, son más seguras en entornos donde no se desea que los datos sean modificados accidentalmente.
# 4. Ocupan menos espacio en memoria que las listas.


# Un tuple puede contener cualquier tipo de dato, incluyendo otras tuplas, listas y diccionarios.
tupla_mixta = (1, "dos", 3.0, (4, 5), [6, 7], {"clave": "valor"})
print(tupla_mixta)

# Para acceder a los elementos de una tupla, se utiliza la indexación, similar a las listas.
print(mi_tupla[0])  # Primer elemento
print(mi_tupla[-1]) # Último elemento
print(mi_tupla[1:4]) # Subtupla desde el índice 1 hasta el 3

# Vaciar el contenido de una tupla en variables individuales
a, b, c, d, e = mi_tupla
print(a)
print(b)
print(c)
print(d)
print(e)
# Si la cantidad de variables no coincide con la cantidad de elementos en la tupla, se generará un error.

# Un tuple puede contener datos repetidos
tupla_repetida = (1, 2, 2, 3, 3, 3)
print(tupla_repetida)
# Para contar cuántas veces aparece un elemento en una tupla, se utiliza el método count()
print(tupla_repetida.count(2))  # Salida: 2
print(tupla_repetida.count(3))  # Salida: 3


# Consultar la posición de un elemento en una tupla
print(tupla_repetida.index(2))  # Salida: 1 (primera aparición de 2)
print(tupla_repetida.index(3))  # Salida: 3 (primera aparición de 3)
# Si el elemento no se encuentra en la tupla, se generará un error.

