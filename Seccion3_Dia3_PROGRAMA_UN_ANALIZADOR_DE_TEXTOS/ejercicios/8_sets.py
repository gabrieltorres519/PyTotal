# Los sets se pueden declarar de dos maneras:
# Usando llaves {}
conjunto1 = {1, 2, 3, 4, 5}
print("Conjunto 1:", conjunto1)
# Usando la función set()
conjunto2 = set([4, 5, 6, 7, 8])
print("Conjunto 2:", conjunto2) 

# La particularidad más importante de los sets es que no permiten elementos duplicados.

conjunto3 = {1, 2, 2, 3, 4, 4, 5}
print("Conjunto 3 (con duplicados):", conjunto3)
print("Conjunto 3 (sin duplicados):", conjunto3)
# Podemos agregar elementos a un set usando el método add()
conjunto1.add(6)
print("Conjunto 1 después de agregar 6:", conjunto1)
# Podemos eliminar elementos usando el método remove()
conjunto2.remove(7)
print("Conjunto 2 después de eliminar 7:", conjunto2)
# También podemos usar discard() que no genera error si el elemento no existe
conjunto2.discard(10)  # No genera error
print("Conjunto 2 después de intentar eliminar 10 (sin error):", conjunto2)

print(2 in conjunto1)  # True
print(10 in conjunto2)  # False

# Para el caso de los sets, el método pop() elimina y retorna un elemento aleatorio del set
elemento_eliminado = conjunto1.pop()
print("Elemento eliminado de Conjunto 1:", elemento_eliminado)
print("Conjunto 1 después de pop():", conjunto1)

# Para vaciar un set, usamos el método clear()  
conjunto3.clear()
print("Conjunto 3 después de clear():", conjunto3)

# Unir dos sets usando union()
conjunto_union = conjunto1.union(conjunto2)
print("Unión de Conjunto 1 y Conjunto 2:", conjunto_union)
# Intersección usando intersection()
conjunto_interseccion = conjunto1.intersection(conjunto2)
print("Intersección de Conjunto 1 y Conjunto 2:", conjunto_interseccion)
# Diferencia usando difference()
conjunto_diferencia = conjunto1.difference(conjunto2)
print("Diferencia de Conjunto 1 y Conjunto 2:", conjunto_diferencia)
# Diferencia simétrica usando symmetric_difference()
conjunto_diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferencia simétrica de Conjunto 1 y Conjunto 2:", conjunto_diferencia_simetrica)


# Objetos no admitidos en sets: listas, diccionarios y otros sets (porque son mutables).
# Objetos admitidos en sets: tuplas y otros objetos inmutables como cadenas y números.
set_con_tupla = {(1, 2), (3, 4)}
print("Set con tuplas:", set_con_tupla)
# set_con_lista = {[1, 2], [3, 4]}  # Esto generaría un error

redes = [ "YouTube", "Facebook", "Twitter", "Whatsapp"] #

print(redes.sort())
         