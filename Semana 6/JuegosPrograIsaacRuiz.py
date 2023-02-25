#inicializan las variables para realizar la suma de cada uno de los tiempos de pits y vueltas
sumaVuelta = 0
sumaPits= 0

#se recorre la cantidad de vueltas que se correran
for indice in range(1,6):
    #se solicita el tiempo por vuelta y por pits
    print("Vuelta numero: ",indice)
    vuelta1 = int(input("Digite el timepo la vuelta: "))
    pits1 = int(input("Ingrese el tiempo de pits: "))
    sumaVuelta += vuelta1
    sumaPits += pits1

#se realiza el promedio por vuelta dividiendo la suma de los tiempos por vuelta dividido entre 5 que es la cantidad de vueltas
promedioVuelta = sumaVuelta//5
#Se realiza el promedio por pit por vuelta sumando los tiempos de los pits dividido entre 5
promedioPits = sumaPits//5
#se calcula el porcentaje total se calcula multiplicando 100 por la suma de pits dividido entre la suma de las vueltas
porcentajeTiempo = 100*sumaPits//sumaVuelta

#Se muestran todos los datos calculados y solicitados

print("El primedio de las vueltas: ", promedioVuelta,"\n El promedio de los pits es: ", promedioPits)
print("El porcentaje de tiempo de pits correspondiente al tiempo recorrido es: ", porcentajeTiempo)



