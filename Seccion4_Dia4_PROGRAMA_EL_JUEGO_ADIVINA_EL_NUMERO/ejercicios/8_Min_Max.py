minimo = min(58, 23, 45, 12, 67)

maximo = max(58, 23, 45, 12, 67)

print("El número mínimo es:", minimo)
print("El número máximo es:", maximo)

lista_numeros = [58, 23, 45, 12, 67]

print("El número mínimo en la lista es:", min(lista_numeros))
print("El número máximo en la lista es:", max(lista_numeros))

# El mínimo y máximo también se pueden usar con cadenas de texto, 
# donde se comparan alfabéticamente y listas de cadenas de texto, 
# donde se compara el primer elemento de cada cadena:

nombres = ["Ana", "Carlos", "Beatriz", "David"]

print("El nombre mínimo es:", min(nombres))
print("El nombre máximo es:", max(nombres))

string = "Hola Mundo"
print("El carácter mínimo en la cadena es:", min(string)) # Imprime el espacio, ya que es el carácter con el valor ASCII más bajo
print("El carácter máximo en la cadena es:", max(string))
# Al tomar los valors acii minimos, primero busca el espacio, luego las letras mayúsculas y finalmente las letras minúsculas. Por eso el espacio es el mínimo y la letra 'u' es el máximo.


# Trabajando con diccionarios, el mínimo y máximo se basan en las claves del diccionario:
edades = {"Ana": 30, "Carlos": 25, "Beatriz": 28, "David": 22}
print("La clave mínima en el diccionario es:", min(edades)) # Imprime "Ana", ya que es la clave con el valor ASCII más bajo
print("La clave máxima en el diccionario es:", max(edades)) # Imprime "David", ya que es la clave con el valor ASCII más alto

# Si quiero los valores y no las claves, puedo usar el método values() del diccionario:
print("El valor mínimo en el diccionario es:", min(edades.values())) # Imprime 22, ya que es el valor más bajo en el diccionario.
print("El valor máximo en el diccionario es:", max(edades.values())) # Imprime 30, ya que es el valor más alto en el diccionario.