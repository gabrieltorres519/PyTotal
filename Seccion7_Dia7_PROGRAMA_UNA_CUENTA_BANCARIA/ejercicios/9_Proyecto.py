import random
from os import system, name

class Persona:
    
    def  __init__(self,nombre,apellido):
        self.nombre = str(nombre)
        self.apellido = str(apellido)
    
class Cliente(Persona):
    
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = str(numero_cuenta)
        self.balance = str(balance)

    def __str__(self):
        return f'Hola {self.nombre} {self.apellido} el saldo para el numero de cuenta {self.numero_cuenta} es de {self.balance}'
    
    def depositar(self,ingreso):
        self.balance = int(self.balance) + ingreso
        print(self)

    def retirar(self,retiro):
        if int(self.balance) < retiro:
            print('No tienes suficiente saldo para realizar esta operación')
        else:
            self.balance = int(self.balance) - retiro
            print(self)

def clear_screen():
    if name == "nt":  # Windows
        system("cls")
    else:  # Unix/Linux/MacOS
        system("clear")

def crear_cliente(nombre,apellido,saldo_inicial):

    mi_cliente = Cliente(nombre,apellido,random.randrange(1,10000),saldo_inicial)
    return mi_cliente

def inicio():

    clear_screen()
    
    nombre = input('Ingrese su nombre: ')
    
    apellido = input('Ingrese su apellido: ')

    saldo_inicial = int(input('Ingrese el saldo inicial para aperturar: '))
    
    mi_cliente = crear_cliente(nombre,apellido,saldo_inicial)

    salir = False

    while salir == False:

        accion = int(input("""
            
            ¿Qué acción desea realizar?
            
            1) Depositar
            2) Retirar
            3) Salir    

        >>>>>> """))

        clear_screen()

        match accion:
            
            case 1:
                ingreso = input('Ingrese el monto a depositar: ')
                mi_cliente.depositar(int(ingreso))
            
            case 2:
                retiro = input('Ingrese el monto a retirar: ')
                mi_cliente.retirar(int(retiro))

            case _:
                salir = True
                print('Saliendo...')

inicio()
