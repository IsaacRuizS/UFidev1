#Se crean las variables
totalpagar = 0

menuprincipal = int(input ("Menú: \n 1- Camisa \n 2- Pantalon \n 3- Sueter \n 4- Falda \n 5- Blusa \n 0- Salir \n"))
while menuprincipal !=0:
    if menuprincipal == 1:
        print ("El precio es de 2000" )
        comprar = int (input("Digite la cantidad que desea comprar:  "))
        totalpagar += comprar *2000
    elif menuprincipal == 2:
        print ("El precio es de 3000" )
        comprar = int (input("Digite la cantidad que desea comprar:  "))
        totalpagar += comprar * 3000
    elif menuprincipal == 3:
        print ("El precio es de 4000" )
        comprar = int (input("Digite la cantidad que desea comprar:  "))
        totalpagar += comprar * 4000
    elif menuprincipal == 4:
        print ("El precio es de 5000" )
        comprar = int (input("Digite la cantidad que desea comprar:  "))
        totalpagar += comprar * 5000
    elif menuprincipal == 5:
        print ("El precio es de 6000" )
        comprar = int (input("Digite la cantidad que desea comprar:  "))
        totalpagar += comprar * 6000
    else:
        print ("Digite una opcion valida")
    menuprincipal = int(input ("Menú: \n 1- Camisa \n 2- Pantalon \n 3- Sueter \n 4- Falda \n 5- Blusa \n 0- Salir \n"))

print ("La cantidad a pagar es:  ", totalpagar)