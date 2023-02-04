#Arreglo para almacenar la edad de las personas
personas = []
#contador para mostrar el numero de persona
numero = 1

#bucle for para recorrer la cantidad de veces del range en este caso 5
for i in range(5):
    i = int(input("Ingrese la edad de la persona numero " + str(numero)+ ": "))
    #se almacena dentro del areglo la edad de la persona ingresada
    personas.append(i)
    #contador de personas
    numero +=1

#se crea la varaible resultado en donde se le almacena la suma de las edades dividia entre la cantidad para dar el promedio
resultado = sum(personas)/len(personas)
print(resultado)