def DetectaDosCeros(*args):

    flag = False
    dos_consecutivos = False

    for arg in args:
        if arg == 0:
            flag = True
        if flag:
            index = args.index(arg)
            if args[index+1] == 0 or args[index-1] == 0:
                dos_consecutivos = True
                break
    
    return dos_consecutivos

print(DetectaDosCeros(1,2,3,5,0,0,45,78,23))

# Recorriendo el arreglo con un contador en lugar de el objeto iterado

def ceros_vecinos(*args):

    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1
    
    return False
        