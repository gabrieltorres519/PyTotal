monedas = 5

while monedas > 0:
    print("Tienes", monedas, "monedas.")
    monedas -= 1
else:
    print("¡Te has quedado sin monedas!")


respuesta = "si"

while respuesta.lower() == "si":
    print("¡Sigue jugando!")
    respuesta = input("¿Quieres seguir jugando? (si/no): ") 
else:
    print("¡Gracias por jugar!")


respuesta2 = "si"

while respuesta2.lower() == "si":
    pass  # Esto es un marcador de posición, no hace nada, sirve para indicar que el bloque de código está vacío

print('Hola')


nombre = input("¿Cuál es tu nombre? ")

for letra in nombre:
    if letra.lower() in "ar":
        print(letra)
        break
    elif letra.lower() in "bc":
        continue # Esto hace que el bucle salte a la siguiente iteración sin ejecutar el código que sigue después de esta línea


    print(letra)