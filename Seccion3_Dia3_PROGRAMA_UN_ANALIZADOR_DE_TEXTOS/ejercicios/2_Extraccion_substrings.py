# A la extracción de substrings en Python se le llama "slicing".
# Consiste en obtener una porción de una cadena de texto (string) utilizando índices.
# La sintaxis básica para hacer slicing es:
# string[inicio:fin:paso]
# Donde:
# - inicio: índice donde comienza el substring (inclusive).
# - fin: índice donde termina el substring (exclusive).
# - paso: (opcional) indica el salto entre caracteres.
# Ejemplos:
texto = "Hola, bienvenidos a Python"

# Recordar que funciona como intervalo abierto en el extremo derecho [inicio, fin), es decir el carácter en la posición 'fin' no se incluye.

# Extraer "Hola"
substring1 = texto[0:4]
print(substring1)  # Salida: Hola       
# Extraer "bienvenidos"
substring2 = texto[6:16]
print(substring2)  # Salida: bienvenido
# Extraer "Python"
substring3 = texto[18:24]
print(substring3)  # Salida: a Pyth
# Extraer cada segundo carácter de "Hola, bienvenidos a Python"
substring4 = texto[0:24:2]
print(substring4)  # Salida: Hl ienid s yhn
# Extraer desde el inicio hasta el carácter en el índice 4
substring5 = texto[:4]
print(substring5)  # Salida: Hola
# Extraer desde el carácter en el índice 18 hasta el final
substring6 = texto[18:]
print(substring6)  # Salida: Python
# Extraer toda la cadena
substring7 = texto[:]
print(substring7)  # Salida: Hola, bienvenidos a Python
# Extraer "Python" usando índices negativos
substring8 = texto[-6:]
print(substring8)  # Salida: Python
# Extraer "bienvenidos" usando índices negativos
substring9 = texto[-18:-8]
print(substring9)  # Salida: bienvenidos    
# Extraer cada tercer carácter desde el final hasta el inicio
substring10 = texto[::-3]
print(substring10)  # Salida: n ei olH
# Estos ejemplos muestran cómo se puede utilizar el slicing para extraer diferentes partes de una cadena de texto en Python.