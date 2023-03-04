#Parte 3, ejercicio 2


#Se solicitan los datos para los caculos
capitalAhorro = float(input("Ingrese el capital de ahorro: "))
tasaInteresAnual = float(input("Ingrese la tasa de interes anual: "))
cantidadAños = float(input("Ingrese la cantidad de años: "))

#Se calcula el capital
capital = capitalAhorro*(1+tasaInteresAnual/100)**cantidadAños

#Se muestra en pantalla el resultado del capital a la tasa de interes ingresada en los años ingresados
print("Capital TOTAL ahorrado ", capitalAhorro, " al ", tasaInteresAnual, " se convierte en: ", round(capital))

#se recorre la cantidad de años para revisar el capital por cada año que pasa
for indice in range(1, int(cantidadAños+1)):
    # Se calcula el capital por año
    capital =capitalAhorro*(1+tasaInteresAnual/100)**indice
    # Se muestra en pantalla el resultado del capital a la tasa de interes ingresada por cada año
    print("En el año: ", indice, " el capital es de: ", round(capital))