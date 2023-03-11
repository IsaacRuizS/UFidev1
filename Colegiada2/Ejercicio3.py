#solicitan e inicializan variables para los calculos
cantidadHuespedes = int(input("Ingrese la cantidad de huespedes: "))
cantidadNoches = 0
total = 0
descuento = 0

#se recorre la cantidad de huespedes que se ingreso
for indice in range(0, cantidadHuespedes):
    print("Huesped numero: ", indice)
    #solicita cantidad de nnoches
    cantidadNoches = int(input("ingrese la cantidad de noches que se hospedara: "))
    total = cantidadNoches * 100
    #si son mas de 3 tiene decuento
    if(cantidadNoches > 3):
        descuento = total *0.05
        total -= descuento
        print("Para el huesped numero: ", indice, "Total con descuento de 5%: ", total)
    else:
        print("Total: ", total)


