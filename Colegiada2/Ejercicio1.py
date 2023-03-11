cantidad  = int(input("Cantidad de empleados a calcular"))
for indice in range(0, cantidad):
    print("Empleado ", indice)
    #Solicita los datos para calcular el nuevo salario
    salarioActual = float(input("Ingrese su salario actual: "))
    tiempoLaboral = int(input("Ingrese la cantidad de anios que tiene de trabajar en la empresa: "))
    #se declara una variable para almacenar el tamaño del aumento
    aumento = 0
    #Se crea una condicion para validar entre cual rango de tiempo esta el numero de años que ingreso
    if(tiempoLaboral >= 0 and tiempoLaboral <= 5):
        #10
        #se calcula el procentaje y se da el resultado en pantalla
        aumento = salarioActual * 0.10
        salarioActual += aumento
        print("El aumento de salario sera de 10%: ", salarioActual)
    elif(tiempoLaboral >= 6 and tiempoLaboral <= 9):
        #15
        aumento = salarioActual * 0.15
        salarioActual += aumento
        print("El aumento de salario sera de 15%: ", salarioActual)
    elif(tiempoLaboral >= 10 and tiempoLaboral <= 15):
        #25
        aumento = salarioActual * 0.25
        salarioActual += aumento
        print("El aumento de salario sera de 25%: ", salarioActual)

    elif(tiempoLaboral > 15):
        aumento = salarioActual * 0.30
        salarioActual += aumento
        print("El aumento de salario sera de 30%: ", salarioActual)


