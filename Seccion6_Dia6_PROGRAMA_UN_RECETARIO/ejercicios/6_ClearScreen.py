# Dependiendo del sistema operativo, el comando para limpiar la pantalla es diferente

from os import system, name

def clear_screen():
    if name == "nt":  # Windows
        system("cls")
    else:  # Unix/Linux/MacOS
        system("clear")

# Ejemplo de uso
print("Esta es una pantalla sucia.")
input("Presiona Enter para limpiar la pantalla...")
clear_screen()
print("La pantalla ha sido limpiada.")



