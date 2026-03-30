# Los diccionarios en Python son estructuras de datos que almacenan pares de clave-valor, como en un diccionario real.
# Son mutables, lo que significa que sus elementos pueden ser modificados después de su creación
# y no mantienen un orden específico hasta Python 3.7, donde se garantiza el orden de inserción.
# Pero en realidad los elementos en él no tienen un orden específico para acceder a ellos, sino que se accede a los valores a través de sus claves.

# Ya que no tienen un orden específico, no se pueden indexar ni fraccionar como las listas o los strings.

# Se utilizan en casos donde necesitamos asociar valores específicos a claves únicas, como almacenar información de un usuario, configuraciones, etc.

diccionario = {'c1': 'valor1', 'c2': 'valor2', 'c3': 'valor3'}
print(type(diccionario))  # <class 'dict'>
print(diccionario)        # {'c1': 'valor1', 'c2': 'valor2', 'c3': 'valor3'}

# Las claves deben ser unicas, aunque los valores pueden repetirse.

resultado = diccionario['c2']
print(resultado)  # 'valor2'

cliente = {
    'nombre': 'Juan',
    'apellido': 'Pérez',   
    'pson': 75,
    'talla': 1.8,
    'es_cliente_activo': True,
    'direcciones': ['Calle 123', 'Avenida 456']
}

consulta_nombre = cliente['nombre']
print(consulta_nombre)  # 'Juan'
consulta_direcciones = cliente['direcciones']
print(consulta_direcciones)  # ['Calle 123', 'Avenida 456']

# diccionarios anidados
empresa = {
    'nombre': 'Tech Solutions',
    'empleados': {
        'e1': {'nombre': 'Ana', 'puesto': 'Desarrolladora'},
        'e2': {'nombre': 'Luis', 'puesto': 'Diseñador'}
    }
}   

empleado_ana = empresa['empleados']['e1']
print(empleado_ana)  # {'nombre': 'Ana', 'puesto': 'Desarrolladora'}
puesto_luis = empresa['empleados']['e2']['puesto']
print(puesto_luis)  # 'Diseñador'   

# diccionarios de listas
curso = {
    'nombre': 'Python Básico',
    'estudiantes': ['Carlos', 'María', 'Luis']
}   
estudiantes = curso['estudiantes']
print(estudiantes)  # ['Carlos', 'María', 'Luis']
primer_estudiante = curso['estudiantes'][0]
print(primer_estudiante)  # 'Carlos'
print(curso['estudiantes'][0].upper())  # 'CARLOS'

# Son mutables, por lo que podemos modificar sus valores
diccionario['c2'] = 'nuevo_valor2'
print(diccionario)  # {'c1': 'valor1', 'c2': 'nuevo_valor2', 'c3': 'valor3'}


# Para conocer todas las claves de un diccionario, podemos usar el método keys()
claves = diccionario.keys()
print(claves)  # dict_keys(['c1', 'c2', 'c3'])

# Para conocer todos los valores de un diccionario, podemos usar el método values()
valores = diccionario.values()
print(valores)  # dict_values(['valor1', 'nuevo_valor2', 'valor3'])

# Cada par clave-valor en un diccionario se llama ítem y el tipo de dato que representa son tuplas o items.
items = diccionario.items()
print(type(items))  # <class 'dict_items'>

# Agregar un nuevo par clave-valor
diccionario['c4'] = 'valor4'
print(diccionario)  # {'c1': 'valor1', 'c2': 'nuevo_valor2', 'c3': 'valor3', 'c4': 'valor4'}
# Recurso: https://claude.ai/public/artifacts/1550b6ba-0e0d-44f0-9307-cf207cc33b67
