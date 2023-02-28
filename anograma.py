from collections import defaultdict
def anogramas(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()
print("Aqui separaras 5 palabras por anogramas")
palabra1 = str(input("Teclea palabra 1 "))
palabra2 = str(input("Teclea palabra 2 "))
palabra3 = str(input("Teclea palabra 3 "))
palabra4 = str(input("Teclea palabra 4 "))
palabra5 = str(input("Teclea palabra 5 "))
palabras = [palabra1,palabra2,palabra3,palabra4,palabra5]
print("Estas son tus palabras: ",palabras)
input("Preciona enter para separarlas por anogramas. ")
print(anogramas(palabras))