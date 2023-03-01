num = [] 
n = input("Cuantos numeros desea ingresar? ")
n2 = int(n)
print("Ingresa",n," Numeros")
for x in range(n2):
    ingresado = input("Ingrese:") 
    agregar = int(ingresado) 
    num.append(agregar)  
num.sort()
print(num) 
falta = []
u= int(num[-1])
for i in range(1,u):
    if i not in num:
        falta.append(i)
print(falta)