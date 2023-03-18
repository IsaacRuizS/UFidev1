#declara el arreglo
butacas = ["","","","","","","","","",""]
#declaracion de variables
nombre = ""
butaca = 0
continuar = True

#recorremos el ciclo hasta que las butacas esten llenas
while continuar == True:
    nombre = input("Escriba un nombre ")
    butaca = int(input("Ingrese el numero de la butaca"))

    #valida que la butaca este vacia
    if(butacas[butaca]!=""):
        print("esa butaca ya esta ocupada")
    else:
        #butaca vacia
        butacas[butaca] = nombre
        print("gracias por su compra")

    continuar = False
    #aqui condiciona la salida del ciclo while valida que las posiciones esten llenas
    for indice in range(10):
        if(butacas[indice]==""):
            continuar = True

print("Las butacas", butacas)


