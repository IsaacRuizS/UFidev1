#Declara el arreglo de los km por dia de la semana
kilometros = [0,0,0,0,0,0,0]
#recorre el arreglo para asignarle los km por dia

for dia in range(7):
    kilometros[dia] = int(input("Digite los kilometros recorridos"))

#totaliza los km por semana
totalKilometros = 0
#recorre el arrelgo para imprimir
for dia in range(7):
    totalKilometros += kilometros[dia]
    print("El dia ", dia+1, "recorrio ", kilometros[dia], "km")
#se muestra el total de km
print("Total km de la semana ", totalKilometros,"km")