# Se trata de poder recibir una cantidad indefinida de "tuplas" {clave:valor} en la función
# de la forma funcion(clave1 = 1, clave2 = 2, clave3 = 3) y ser accesadas desde dentro como
# si se tratara de un diccionario

def suma(**kwargs):
    print(kwargs)
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

suma(clave1 = 1, clave2 = 2, clave3 = 3)


# También se pueden pasar literalmente listas y diccionarios
print('______________________________________________________________________________________________________________\n')

def prueba(num1, num2, *args, **kwargs):
    
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:    
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [100, 200, 300, 400]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15,30,*args,**kwargs)


# Para contar la cantidad de argumentos ingresados en la función

def cantidad_atributos(**kwargs):
    return len(kwargs.items())

diccionario_atributos = {'v1':'1','v2':'2','v3':'3'}

conteo = cantidad_atributos(**diccionario_atributos)

print(f'La cantidad de atributos (clave:valor) es: {conteo}')