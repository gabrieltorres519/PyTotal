def suma():
    # En el siguiente código si ingresamos datos que no sean un entero dará error
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")


try:
    # Código que queremos probar
    suma()
except:
    # Código a ejecutar si hay un error
    print('Algo no ha salido bien con la funcion suma()')
else:
    # Código a ejecutar si no hay ningún error
    print('Salio bien todo con la funcion suma()')
finally:
    # Código que se va a ejecutar de todos modos (este no tiene tanta aplicacion)
    print('Eso fue todo, con o sin errores')



# Específico para los tipos de errores (documentación: https://docs.python.org/3/library/exceptions.html)
try:
    suma()
except TypeError:
    print('Estas intentando concatenar tipos de datos distintos')
except ValueError:
    print('Ese no es un numero')
else:
    print('No hubo errores')
finally:
    print('Eso fue todo, con o sin errores')


# Pequeña automatización de una prueba en un ciclo

def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f'Se ha ingresado el número {numero} correctamente')
            break

    print("Gracias")

pedir_numero()
