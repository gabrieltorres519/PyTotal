# Los "decoradores" permiten crear diferentes tipos de métodos
# - Métodos de instancia o métodos normales de objetos instanciados
# - Métodos de clase @classmathod
# - Métodos estáticos @staticmethod

# Ejemplo de método de instancia que solo se pueden usar con objetos instanciados
class Ejemplo:
    
    def __init__(self):
        pass

    def mi_metodo(self):
        print('Algo')

ejemplo_instancia = Ejemplo()

ejemplo_instancia.mi_metodo()


# Ejemplo de método de clase
class Ejemplo2:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod   # Destacar que los métodos de clase solo pueden modificar variables de clase, no las del constructor para objetos instanciados
    def from_string(cls, date_string): # En lugar de poner self ponemos cls (class)
        # Constructor alternativo para crear un objeto Ejemplo2 de un string
        year, month, day = map(int, date_string.split('-'))
        print(year, month, day)
        return cls(year, month, day) # Retorna una instancia de la clase (cls)

# Los métodos de  clase se pueden utilizar sin instanciar un objeto de la misma, directamente con la clase:
Ejemplo2.from_string('2025-07-11')


# Ejemplo de método estático
class Ejemplo3:

    def __init__(self):
        pass

    @staticmethod  # Destacar que los métodos estaticos solo pueden modificar variables de clase, no las del constructor para objetos instanciados
    def mirar(): # ni sefl ni cls, así se evita que modifiquen las instancias 
        print("Está mirando...")

# Los métodos estáticos se pueden utilizar sin instanciar un objeto de la misma, directamente con la clase:
Ejemplo3.mirar()

