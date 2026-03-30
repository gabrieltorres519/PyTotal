mi_archivo = open('Prueba.txt')

# print(mi_archivo)

# print(mi_archivo.read())

# print(f'\n {mi_archivo.readline()}')

# Como cada línea son strings, se pueden utilizar todos sus métodos
# una_linea = mi_archivo.readline()
# print(una_linea.upper())

# una_linea = mi_archivo.readline()
# print(una_linea.rstrip())

# una_linea = mi_archivo.readline()
# print(una_linea)

# Usando un ciclo para extraer cada línea del archivo
# for linea in mi_archivo:
#     print("Aquí dice: " + linea)

todas = mi_archivo.readlines() # Un array con las líneas del texto

todas = todas.pop()

print(todas)


mi_archivo.close() # Liberando la memoria ram

