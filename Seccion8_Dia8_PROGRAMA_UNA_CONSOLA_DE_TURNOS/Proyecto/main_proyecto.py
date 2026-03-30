"""
Turnero de comercio

Áreas:

    - Perfumería
    - Farmacia 
    - Cosmética

- Inicial del área y número de turno para el boleto
- Preguntar siempre por otro turno o terminar
- Llevar cuenta de cuántos turnos se han dado para cada área (Generadores)
- Llevar texto antes y después del turno para el cliente (Decoradores)

* Módulo de números (todos los decoradores y el generador para turnos)
* Módulo principal con las clases o funciones (importar el módulo de los números)
* Manejo de errores
"""
import numeros

def principal():
    """Función principal del proyecto"""
    numeros.limpiar_pantalla()
    continuar = True
    turnos = [0,0,0]

    while continuar:

        print("""
            Seleccione el área para tomar un turno:
              
              1. Perfumería
              2. Farmacia
              3. Cosmética
              4. Salir
        """)

        try:
            seleccion = int(input(': '))
        except ValueError:
            numeros.limpiar_pantalla()
            print('Ingrese un numero válido')
        else:
            if seleccion == 1:
                print('Ha seleccionado Perfumería')
                turnos[0] = numeros.proceso(1,turnos[0],numeros.turnos_area,numeros.decorar_turnos)
            elif seleccion == 2:
                print('Ha seleccionado Farmacia')
                turnos[1] = numeros.proceso(2,turnos[1],numeros.turnos_area,numeros.decorar_turnos)
            elif seleccion == 3:
                print('Ha seleccionado Cosmética')
                turnos[2] = numeros.proceso(3,turnos[2],numeros.turnos_area,numeros.decorar_turnos)
            elif seleccion == 4:
                numeros.limpiar_pantalla()
                print('Gracias por usar el turnero')
                continuar = False
            else:
                numeros.limpiar_pantalla()
                print('Opción no válida, intente de nuevo')

principal()
