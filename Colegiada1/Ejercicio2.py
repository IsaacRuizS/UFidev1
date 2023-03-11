#se ionicializan  las variables pare hacer los calculos
valorPantalon = 0
descuento = 0
montoTotal = 0
totalPantalones= 0

#se piden los datos
totalPantalones = int(input("Cantidad de pantalones comprados: "))
valorPantalon= float(input("ingrese el valor del pantalon: "))
#se caculca y se muestra el monto total
montoTotal = totalPantalones * valorPantalon
print("monto Total sin descuento: ", montoTotal)
#se le hace el descuento dependiendo la cantidad de pantalones compradas
if(totalPantalones >=1 and totalPantalones <= 5):
    #se calcula el procentaje que se descontara del monto total y se muestra los resultados
    descuento = montoTotal * 0.125
    montoTotal -= descuento
    print("total del decuento 12.5%: ", descuento)
    print("Total aplicando el descuento: ", montoTotal)
    #12.5
elif(totalPantalones >=6 and totalPantalones <= 8):
    #20
    descuento = montoTotal * 0.2
    montoTotal -= descuento
    print("total del decuento 12.5%: ", descuento)
    print("Total aplicando el descuento: ", montoTotal)
elif(totalPantalones > 8):
    #31.5
    descuento = montoTotal * 0.325
    montoTotal -= descuento
    print("total del decuento 12.5%: ", descuento)
    print("Total aplicando el descuento: ", montoTotal)