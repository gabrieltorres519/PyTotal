# Ejercicio 1: Método index(). Recordar que un string es una secuencia inmutable de caracteres.
# Estan ordenados con indices que comienzan en 0.

mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)

# Del final del string hacia atrás utilizamos indices negativos 
resltado = mi_texto[-1]
print(resltado)

# El método index() nos permite encontrar la posición de un caracter o una secuencia de caracteres
resultado = mi_texto.index("p")
print(resultado)

# Se pueden buscar substrings (secuencias de caracteres) pero solo nos devolverá la posición del primer caracter del substring
resultado = mi_texto.index("prueba")
print(resultado)

# Si el substring no se encuentra en el string, se genera un error, por ejemplo si buscamos Prueba con mayuscula inicial en lugar de prueba
# resultado = mi_texto.index("Prueba")
# print(resultado)  # Esto generará un ValueError

# Index solo busca de izquierda a derecha

# Comenzar la búsqueda desde un índice específico
resultado = mi_texto.index("e", 3)  # Buscar 'e' comenzando desde el índice 3
print(resultado)

# Se puede especificar un rango para la búsqueda
resultado = mi_texto.index("e", 3, 10)  # Buscar 'e' entre los índices 3 y 10
print(resultado)

# Cuando no se encuentra el substring en el rango especificado, se genera un error siempre

# Existe otro método que hace exactamente lo mismo que index() pero realiza la búsqueda de derecha a izquierda, es rindex()
resultado = mi_texto.rindex("e")  # Buscar 'e' desde el final del string
print(resultado)