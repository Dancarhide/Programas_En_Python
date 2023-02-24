import datetime

# Obtenemos la fecha actual
fechaActual = datetime.datetime.now().date()

# Mostramos el día de hoy en formato mes, día y año por separado
mes = fechaActual.month
dia = fechaActual.day
año = fechaActual.year

diaU = int(input(" Teclea el dia de tu nacimiento "))
mesU = int(input(" Teclea el mes de tu nacimiento "))
añoU = int(input(" Teclea el año de tu nacimiento "))



print("Hoy es: ",fechaActual.today())

if mes>=mesU:
    if dia>=diaU:
        edad = año-añoU
        print("Tu edad es: ",edad)
    elif dia<diaU:
        edad = año-añoU-1
        print("Tu edad es: ",edad)
elif mes<mesU:
    edad = año-añoU-1
    print("Tu edad es: ",edad)
    
    






