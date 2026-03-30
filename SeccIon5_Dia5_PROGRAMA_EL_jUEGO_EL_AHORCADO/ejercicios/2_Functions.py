# Los métodos de los objetos nativos de python son funciones, pero no se llaman funciones, se llaman métodos.

# Por ejemplo, el método upper() es un método de los objetos de tipo string, y se llama así porque se llama 
# con un punto después del objeto, como en "hola".upper()

# Sin embargo, también podemos crear nuestras propias funciones, que son bloques de código que realizan una 
# tarea específica y que pueden ser reutilizados en diferentes partes de nuestro programa.

# Para crear una función en python, utilizamos la palabra clave def seguida del nombre de la función y paréntesis.

# Por ejemplo, si queremos crear una función que sume dos números, podemos hacerlo de la siguiente manera:

def sumar(a, b):
    return a + b
# En este ejemplo, hemos creado una función llamada sumar que toma dos parámetros, a y b, y devuelve la suma 
# de ambos.
# Para llamar a esta función, simplemente escribimos su nombre seguido de los argumentos entre paréntesis, 
# como en sumar(2, 3), lo que devolverá 5.
# Las funciones pueden tener cualquier cantidad de parámetros, e incluso pueden no tener ninguno. Por ejemplo, 
# si queremos crear una función que no reciba parámetros, podemos hacerlo así:

def saludar():
    return "Hola, mundo!"

# Para llamar a esta función, simplemente escribimos su nombre sin argumentos, como en saludar(), lo que devolverá "Hola, mundo!"

# Funcion para desempacar tuples 

precios_cafe = [('capuchino', 1.5), ('Expresso',1.2), ('Moka', 1.9)]

for elemento in precios_cafe:
    print(elemento)

for cafe, precio in precios_cafe:
    print(f"El precio del {cafe} es {precio} euros")


def cafe_mas_caro(lista_precios):
    
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in lista_precios:

        if precio > precio_mayor:

            precio_mayor = precio
            cafe_mas_caro = cafe

    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El café más caro es el {cafe} y cuesta {precio} euros")
