import random
num1 = random.randint(1, 10) 
num2 = random.randint(1, 10) 
op = random.randint(1, 2)

if(op==1):
    pcop= num1
else:
    pcop = num2
print(pcop)
print("Los numeros a elijir son ",num1," y ",num2)
us = int(input("= "))
if us == pcop:
    print("Genial! era este el correcto")
else:
    print("Perdistes!! era el numero",pcop)
