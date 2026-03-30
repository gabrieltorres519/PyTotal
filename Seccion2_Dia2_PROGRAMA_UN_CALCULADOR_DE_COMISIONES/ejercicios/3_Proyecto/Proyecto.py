nombre = input("Ingrese su nombre: ")
ventas = input("Ingrese el monto total de ventas realizadas por usted: ")

print(f"Hola {nombre}, el total de comisiones que te corresponde es de: $ {round(float(ventas)*0.13, 2)}" )

