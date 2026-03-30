# *args es utilizado para cuando no se conoce la cantidad de argumentos que una función va a recivir
# básicamente una lista de tamaño variable que es iterable dentro de la funcion


def sumatoria(*args):
    return sum(args)

print(sumatoria(1,2,3,4,5,6,7))

