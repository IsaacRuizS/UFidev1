#Ejercicio 6
#se toman los datos a utilizar y se almacenan en variables
distancia = int(input("Ingrese la distancia de su casa a la universidad: "))
costo = int(input("Ingrese el costo por kilometro: "))
diaSemana = int(input("Ingrese la cantidad de dias a la semana que va a la Universidad: "))

#se realiza la operacion para obtener el costo total
costoTotal = ((((distancia*2)*costo)*diaSemana)*15)
#se muestra resultado
print("El costo total asumiendo que son 15 semanas de ida y vuelta es de: ", costoTotal)