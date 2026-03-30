from random import *
 
def pedir_validar_letra(palabra):
    
    letra = input('Ingrese una letra: ')
    abecedario = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

    if letra in abecedario:

        palabra = list(palabra)
        contador = 0
        array_indices = []
        
        if letra in palabra:
            
            for letra_for in palabra:
                
                if palabra[contador] == letra:

                    array_indices.append(palabra.index(letra))

                contador += 1

            contador = 0

        return [letra, palabra , array_indices]
    
    else:
        
        print('\n No ha ingresado una letra...\n')
        resultado = pedir_validar_letra(palabra)

        return resultado

def constructor_palabra_usuario(letra_indices_y_palabra):
    
    intentos_restantes = len(letra_indices_y_palabra[1])
    tamano_palabra = len(letra_indices_y_palabra[1])
    aciertos_palabra = []

    for i in range(tamano_palabra):
        aciertos_palabra.append('_')

    while intentos_restantes > 0:

        
        if len(letra_indices_y_palabra[2]) == 0:
            
            print('La letra seleccionada no se encuentra en la plabra')
            
            intentos_restantes -= 1 

            if intentos_restantes == 0:
                print('No consiguió completar la palabra')
                break

            print(f'Tienes {intentos_restantes} vidas restantes')

            letra_indices_y_palabra = pedir_validar_letra(letra_indices_y_palabra[1])

        else:
            
            print(f'Tienes {intentos_restantes} vidas restantes')

            aciertos_palabra[letra_indices_y_palabra[2][0]] = letra_indices_y_palabra[0]

            print(''.join(aciertos_palabra))

            if '_' not in aciertos_palabra:
                print('Ha ganado')
                break

            letra_indices_y_palabra = pedir_validar_letra(letra_indices_y_palabra[1])

palabra_seleccionada = choice(['Hola','Mundo','Con','Python','Basic'])

resultado_turno = pedir_validar_letra(palabra_seleccionada)

constructor_palabra_usuario(resultado_turno)

