from random import shuffle

# Lista inicial
palitos = ['-','--','---','----','-----']

# mezclar palitos
def mezclar_palitos(lista_palitos):
    shuffle(lista_palitos)
    return lista_palitos    

# pedirle intento
def probar_suerte():
    intento = '' 
    while intento not in ['1','2','3','4','5']:
        intento = input('Escoge un palito (numero del 1 al 5) ')

    return int(intento)

# comprobar intento
def chequear_intento(lista_palitos, intento):
    if lista_palitos[intento-1] == '-':
        print('¡Perdiste, a lavar los platos!')
    else:
        print(f'¡No te tocará lavar los platos!')

    print(f'El palito que te tocó fue: {lista_palitos[intento-1]}')

palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion) 


from random import randint

# Lanzar los dados
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return (dado1, dado2)

# Evaluación de qué salió en el lanzamiento
dado1, dado2 = lanzar_dados()

print(dado1)
print(dado2)
print(dado1 + dado2)


def evaluar_jugada(dado1, dado2):

    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        print(f'La suma de tus dados es {suma_dados}. Lamentable')
    elif suma_dados > 6 and suma_dados < 10:
        print(f'La suma de tus dados es {suma_dados}. Tienes buenas chances')
    elif suma_dados > 10:
        print(f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora')
        
evaluar_jugada(dado1, dado2)
        