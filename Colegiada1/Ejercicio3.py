#solicitan e inicializan variables para los calculos
cantidadNoches = 0
total = 0
descuento = 0

#solicita cantidad de nnoches
cantidadNoches = int(input("ingrese la cantidad de noches que se hospedara: "))
total = cantidadNoches * 100
#si son mas de 3 tiene decuento
if(cantidadNoches > 3):
    descuento = total *0.05
    total -= descuento
    print("Total con descuento de 5%: ", total)
else:
    print("Total: ", total)


