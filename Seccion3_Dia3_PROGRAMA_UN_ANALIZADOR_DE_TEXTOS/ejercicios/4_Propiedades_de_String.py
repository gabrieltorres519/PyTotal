# Propiedades de los strings

# Son inmutables
mi_string = "Hola"
print(mi_string[0])  # Imprime 'H'
# mi_string[0] = 'h'  # Esto causaría un error porque los strings son inmutables
# mi_string.replace('H', 'h')  # Esto crea un nuevo string, no modifica el original

# Concatención
saludo = "Hola"
nombre = "Mundo"
frase_completa = saludo + " " + nombre
print(frase_completa)  # Imprime 'Hola Mundo'

# Repetición
repetido = "Hola " * 3  
print(repetido)  # Imprime 'Hola Hola Hola '

# División de textos largos
texto_largo = """Este es un texto largo
que se extiende
en varias líneas."""
print(texto_largo)

# Saber con un valor booleano si un texto es parte de otro
frase = "El cielo es azul"
print("cielo" in frase)  # Imprime True
print("verde" in frase)  # Imprime False
print("verde" not in frase)  # Imprime True

# Longitud de un string
mi_texto = "Hola Mundo"
print(len(mi_texto))  # Imprime 10

# Índices negativos
print(mi_texto[-1])  # Imprime 'o'