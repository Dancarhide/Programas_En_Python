usuarios = ["Dante", "Canon", "juan", "Dancar"]
contraseñas = ["Mickey","2004","juanlv","Hola143"]
print("Elije una opcion")
print("1) Comprobar contraseña")
print("2) Crear usuario")
print("3) Eliminar usuario")
print("4) Salir")
opc =input("Opcion: ")
contador = 0

while opc != "0":
    if contador >= 1:
        print("Elije una opcion")
        print("1) Comprobar contraseña")
        print("2) Crear usuario")
        print("3) Eliminar usuario")
        print("0) Salir")
        opc =input("Opcion: ")
    contador = contador+1

    if opc == "1":
        print(usuarios)
        us = input("Usuario: ")
        co = input("Contraseña: ")
        if us in usuarios:
            posision = usuarios.index(us)
            if co == contraseñas[posision]:
                print("contraseña correcta ")
            else:
                print("usuario o contraseña incorrecta ")
        else:
            print("Usuario o contraseña incorrecta ")
    elif opc == "2":
        use = input(" Usuario: ")
        con = input("Contraseña:")
        usuarios.append(use)
        contraseñas.append(con)
        print(usuarios)

    elif opc == "3":
        print(usuarios)
        eliminar = input("Elije usuario a eliminar: ")
        contra = input("Teclea la contraseña del us: ")
        posision = usuarios.index(eliminar)
        if contra == contraseñas[posision]:
            print("has eliminado al usuario: ",eliminar)
            pos = usuarios.index(eliminar)
            posi = int(pos)
            usuarios.remove(eliminar)
            contraseñas.pop(posi)
           
        else:
            print("Contraseña incorrecta")
        


    elif opc == "0":
        print("Adios")
    else:
        print("Opcion incorrecta")



