def mi_generador():
    
    x = 0
    
    while True:
        x+=1
        yield x


generador = mi_generador()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


def mi_generador():

    y = 0
    while True:
        y+=1 
        result = y*7
        yield result 
        

generador = mi_generador()

print('\n')
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))



def mi_generador_resta_vidas():
    
    vidas = 4
    
    while vidas >= 0:
        
        vidas-=1
        
        match(vidas):
            case 3:
                yield "Te quedan 3 vidas"
            case 2:
                yield "Te quedan 2 vidas"
            case 1:
                yield "Te quedan 1 vida"
            case 0:
                yield 'Game Over'
            case _:
                break

generador = mi_generador_resta_vidas()
 
print('\n')
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


# Una opción más adecuada a la funcionalidad de los decoradores para la resta de vidas es la siguiente

def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
 
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
 
perder_vida = mensaje()

print('\n')
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
