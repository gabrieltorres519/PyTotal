
# Ejemplo de decorar una función

# Conceptos importantes: 
# - Almacenaje de una función en una variable
# - Definición de funciones dentro de una función y lógica para retornarlas (retorno de funciones)

def decorar_funcion(funcion):  #  Función que devuelve una función

    def funcion_decoradora(palabra):
        print("\nAntes de ejecutar la función decoradora")
        funcion(palabra) # Función recibida que será "decorada"
        print("Después de ejecutar la función decoradora\n")

    return funcion_decoradora


def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

    
mayuscula_decorada = decorar_funcion(mayusculas) #  Función que devuelve una función
minuscula_decorada = decorar_funcion(minusculas)    

mayuscula_decorada('Texto para mayusculas') # Función decoradora retornada 
minuscula_decorada('Texto para minusculas')



# Lo mismo que lo anterior pero usando la funcion como decorador como tal 
@decorar_funcion # Misma funcion creada para decorar
def mayusculas2(texto):
    print(texto.upper())

@decorar_funcion
def minusculas2(texto):
    print(texto.lower())

mayusculas2('Texto para mayusculas2')
minusculas2('Texto para minusculas2')
