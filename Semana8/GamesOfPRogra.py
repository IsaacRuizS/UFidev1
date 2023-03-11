#Funcion para solicitar el salario actual y el dia que trabaja
def solicitarDatos():
    salarioActual = float(input("ingrese el salario actual"))
    diaLaboral = input("ingrese el dia en que usted trabaja: ").lower()
    #se llama a la funcion para realizar los calculos enviando por parametros los datos solicitados anteriormente
    calculoSalario(salarioActual, diaLaboral)

#funcion para calcular el aumento de salario segun los dias laborales
def calculoSalario(salarioActual, diaLaboral):
    #si el dia es igual a lunes martes o miercoles aumentara el salario en 10%
    if (diaLaboral == "lunes" or diaLaboral == "martes" or diaLaboral == "miercoles"):
        # aumento de 10%
        aumento = salarioActual * 0.10
        resultadoTotal = salarioActual + aumento
        print("Salario con el aumento: ", resultadoTotal)
    # si el dia es igual a jueves viernes o sabado aumentara el salario en 20%
    elif (diaLaboral == "jueves" or diaLaboral == "viernes" or diaLaboral == "sabado"):
        # aumento de 20%
        aumento = salarioActual * 0.20
        resultadoTotal = salarioActual + aumento
        print("Salario con el aumento: ", resultadoTotal)
    # si el dia es igual a domingo aumentara el salario en 40%
    elif (diaLaboral == "domingo"):
        # Aumenta un 40%
        aumento = salarioActual * 0.40
        resultadoTotal = salarioActual + aumento
        print("Salario con el aumento: ", resultadoTotal)

    else:
        print("No ingresaste un dia valido")
        #si no se identifico el dato se solicita de nuevo
        solicitarDatos()

#Se inicia el sistema llamando a la funcion
solicitarDatos()