# Existen dos formas de generar valores booleanos en Python.
# Con una comparación, expresión o función que retorne True o False.
# Con Bool() que convierte un valor a su equivalente booleano.
valorBooleano = True
print(type(valorBooleano))
print(valorBooleano)


# Se pueden utilizar operadores lógicos y matemáticos para comparaciones que generan valores booleanos.
# Puede ser directamente o explícitamente con la función bool().
numero = 10
comparacion = numero > 5
print(type(comparacion))
print(comparacion)
comparacion2 = bool(numero < 5)
print(type(comparacion2))
print(comparacion2)
# También se pueden generar valores booleanos con la función bool() a partir de otros tipos de datos.
# Los valores que se consideran False son: None, False, 0, 0.
# Cadenas vacías, listas vacías, tuplas vacías y diccionarios vacíos.
valor1 = ""
valorBooleano1 = bool(valor1)
print(type(valorBooleano1))
print(valorBooleano1)
valor2 = [1,2,3]
valorBooleano2 = bool(valor2)
print(type(valorBooleano2))
print(valorBooleano2)


# También se pueden generar valores booleanos con el operador in.


lista = [1,2,3,4]

control = 5 in lista

print(type(control))
print(control)


array = [1,2,3,4]

print(array[-1:0:-1])  # Salida: [4, 3, 2, 1]
