"""Módulo con las funciones necesarias para el generador de turnos"""
import os

# Función para decorar el numero de turno del área en cuestión
def decorar_turnos(contenido,area_num):
    """Función para decorar el numero de turno del área en cuestión"""

    def funcion_decoradora():
        print('    Su turno es\n')
        match(area_num):
            case 1:
                print(f'P-{str(contenido)}')
            case 2:
                print(f'F-{str(contenido)}')
            case 3:
                print(f'C-{str(contenido)}')
        print('\nAguarde y será atendido')

    return funcion_decoradora

# Generador de turnos para las áreas
def turnos_area(turno):
    """Generador de turnos para las áreas"""
    while True:
        turno+=1
        yield turno

# Función para limpiar la pantalla según el sistema operativo
def limpiar_pantalla():
    """Función para limpiar la pantalla según el sistema operativo"""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y macOS
        os.system('clear')

# Función para imprimir el número de turno del área específica y devolverlo
def proceso(area_num,turno,area,decorador):
    """Función para imprimir el número de turno del área específica y devolverlo"""
    limpiar_pantalla()
    mi_generador = area(turno)
    dato = next(mi_generador)
    imprimir = decorador(dato,area_num)
    imprimir()
    return dato
