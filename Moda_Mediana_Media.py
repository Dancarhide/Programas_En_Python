#aqui puedo sacar la moda de una lista
import statistics

n = int(input("Ingrese la cantidad de datos a ingresar: "))

lista = []
for i in range(n):
    dato = input("Ingrese el elemento {}: ".format(i+1))
    lista.append(dato)
print("Los datos son:", lista)
lista = [int(num) for num in lista]

#sum para sumar los numeros de la lista y len cantidad de caracteres
media = sum(lista) / n
print("La media es: ", media)
#ordenar arreglo
lista.sort()

mediana = n/2
entero = int(mediana)
mitad = entero-1
medianxx = lista[mitad]
medianax= lista[entero]
if n % 2 == 0:
    medianaFinal= (medianax+medianxx)/2
    print("La mediana es: ",medianaFinal)
else:
    print("La mediana es: ",medianax)
moda = statistics.mode(lista)
print("La moda es: ",moda)


