
texto = "Este es el texto de Federico"

resultado = texto

print(resultado)

# Ejercicio 1: Convertir todo el texto a mayúsculas
resultado_mayusculas = texto.upper()
print("Texto en mayúsculas:", resultado_mayusculas)

# Ejercicio 2: Seleccionar solo un elemento del texto y pasarlo a mayúsculas
primer_palabra_mayusculas = texto[0].upper()
print("Primera letra en mayúsculas:", primer_palabra_mayusculas)

# Ejercicio 3: Seoparación de elementos del texto en una lista (array de palabras)
lista_palabras = texto.split()  
print("Lista de palabras:", lista_palabras)

# Ejercicio 4: Separacion de elementos del texto en una lista basada en un caracter específico e ignorando dicho caracter
lista_sin_e = texto.split("t")
print("Lista sin 'e':", lista_sin_e)

# Ejercicio 5: Unión de elementos de una lista en un solo texto con un caracter específico entre ellos
a = "Aprender"
b = "Python" 
c = "es"
d = "genial"
e = "-".join([a, b, c, d])
print("Texto unido con guiones:", e)

# Ejercicio 6: Encontrar la posición de un elemento específico dentro del texto
posicion_federico = texto.find("Federico")
print("Posición de 'Federico':", posicion_federico)

# Ejercicio 7: Reemplazar un elemento específico del texto por otro
texto_reemplazado = texto.replace("Federico", "Python")
print("Texto con reemplazo:", texto_reemplazado)