import datetime # No nombrar el archivo del código igual que la librería

"""Fecha y hora actuales"""
minutos = datetime.datetime.now().time().minute

print(minutos)

"""Trabajo con horas"""
mi_hora = datetime.time(17,35,50,1000) # Objeto para dar formato a la hora que deseamos imprimir o usar
print(mi_hora) 
print(mi_hora.hour)
print(mi_hora.minute)
print(mi_hora.second)
print(mi_hora.microsecond)


"""Trabajo con fechas"""
mi_dia = datetime.date(2020,3,16) # Objeto para dar formato a la fecha que deseamos imprimir o usar
print(mi_dia)
print(mi_dia.year)
print(mi_dia.ctime())
print(mi_dia.today())


"""Para utilizar fecha y hora juntas"""
from datetime import datetime

mi_fecha = datetime(2020,3,16,17,35,50,1000)
print(mi_fecha)


"""Modificar fecha y hora actuales"""
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)


"""Calcular tiempo entre horas y fechas"""
from datetime import date

nacimiento = date(1999,9,28)
graduacion = date(2024,7,20)

profesional = graduacion - nacimiento

print(profesional.days)

despierta = datetime(2020,3,16,8,5)
duerme = datetime(2020,3,16,22,30)

vigilia = duerme - despierta

print(vigilia)
print(vigilia.seconds)


