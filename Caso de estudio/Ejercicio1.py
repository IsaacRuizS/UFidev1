#Primera parte

#Solicitan los datos
year = int(input("Ingrese un año: "))
born = int(input("Ingrese su año de nacimiento: "))
#Se calculan los años que se tendra en el año ingresado
totalYears = year - born

#se realiza una condicion que si el calculo de la edad es menor a 18 indique que es menor de edad y si no es mayor de edad
if(totalYears < 18):
    #Se muestra el resultado
    print("En el año ", year, " cumpliras ", totalYears, " y seras menor de edad")
else:
    #Se muestra el resultado
    print("En el año ", year, " cumpliras ", totalYears, " y seras mayor de edad")
