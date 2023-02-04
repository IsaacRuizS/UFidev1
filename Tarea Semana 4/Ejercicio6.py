#Ejercicio 6
distancia = int(input("Ingrese la distancia de su casa a la universidad: "))
costo = int(input("Ingrese el costo por kilometro: "))
diaSemana = int(input("Ingrese la cantidad de dias a la semana que va a la Universidad: "))

costoTotal = ((((distancia*2)*costo)*diaSemana)*15)

print("El costo total asumiendo que son 15 semanas de ida y vuelta es de: ", costoTotal)