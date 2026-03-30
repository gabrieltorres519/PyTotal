# Juego adivina el número
# El programa genera un número aleatorio entre 1 y 100, y el usuario tiene
# que adivinarlo. El programa le dará pistas al usuario si el número es
# mayor o menor que su intento, y contará el número de intentos que le
# tomó adivinar el número.
from random import randint

counter = 8
number = randint(1, 100)
seguir = 's'
i = 0

while seguir.lower() == 's':

    while counter > 0:
        guess = int(input('Adivina el número entre 1 y 100: '))
        match guess:
            case _ if guess < number:
                print('El número es mayor')
                i += 1
                counter -= 1
            case _ if guess > number:
                print('El número es menor')
                i += 1
                counter -= 1
            case _ if guess == number:
                print(f'¡Felicidades! Adivinaste el número en {i + 1} intentos')
                i += 1
                counter -= 1
                break
            case _:
                print('Número inválido')
                i += 1
                counter -= 1
    i = 0
    seguir = str(input('¿Quieres jugar de nuevo? (s/n): '))

