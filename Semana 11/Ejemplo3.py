#declaracion de la matriz para el control de la agenda de entrevistas
entrevistas = [["" for colmna in range(9)] for fila in range(5)]

nombre=" "

#ciclo hasta que nombre sea vacio
while nombre != "":
    # solicita al usuario el dnombre del entrevistado
    nombre = input("Ingrese el nombre de la persona entrevisada: ")
    if nombre!= "":
        #solicita al usuario el dia y la hora para la entrevista
        dia= input("Digite el dia de la semana de (1-5): ")
        hora = input("Digite la hora del dia (9-17):")
        #calcula el dia y la columna en base al dia y la hora
        fila = int(dia) -1
        columna = int(hora) -9

        #valida la posicion si esta vacia
        if entrevistas[fila][columna]!="":
            #solicita el entrevistado y lo muestra
            entrevistado = entrevistas[fila][columna]
            print("El dia y la hora ya estan agendados para", entrevistado)
        else:
            #si esta vacia le asigna nombre a la posicion
            entrevistas[fila][columna] = nombre
            print("El dia y la hora han sido agendados")
print("entrevista", entrevistas)