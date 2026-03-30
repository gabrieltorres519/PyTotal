# El pirmer numero es intervalo cerrado, el segundo numero es intervalo abierto
# esto es, el numero 1 esta incluido pero el numero 10 no esta incluido
for numero in range(1, 10):
    print(numero)


# Cuando es necesaria una lista muy grande de numeros, es mejor usar la funcion range() que crear una lista con todos los numeros
lista = list(range(1, 101))  # Crea una lista con los números del 1 al 100

print(lista)

# Tambien puedes decidir el salto entre los numeros, por ejemplo, si quieres solo los numeros pares del 1 al 100
numeros_pares = list(range(2, 101, 2))  # Crea una lista con los números pares del 1 al 100
print(numeros_pares) 