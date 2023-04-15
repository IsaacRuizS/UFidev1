#importamos la liberia para utilizar numeros aleatorios
import random

#Declaramos el arreglo
ordenBurbuja = []
#Pedimos el tamaño del arreglo
tamaño = int(input("Ingrese el tamaño del arreglo: "))
#Declaramos un iterador para rellenar el arreglo
iterador = 0

#Mientras el iterador sea menor al tamaño indicado
while iterador < tamaño:
    #se declara una variable con el numero aleatorio a agregar
    numeroRandom = random.randrange(1, 1000)
    #se agrega el valor al arreglo
    ordenBurbuja.append(numeroRandom)
    #Se incrementa en uno el iterador
    iterador +=1
#mostramos el arreglo sin ordenar
print("Sin ordenar",ordenBurbuja)

#variable para validar que se complete todo el ordenamiento
intercambio = True
while intercambio:
    intercambio = False
    #se recorre cada posicion del arreglo
    for elemento in range(len(ordenBurbuja) -1 ):
        #si la primera posicion es mayor a la siguiente se intercambian los valores
        if(ordenBurbuja[elemento] > ordenBurbuja[elemento+1]):
            #varaible para almacenar el valor mayor
            elementoMayor = ordenBurbuja[elemento]
            #se intercabian los valores
            ordenBurbuja[elemento] = ordenBurbuja[elemento+1]
            ordenBurbuja[elemento + 1] = elementoMayor
            #se continua con el intercambio
            intercambio = True

#mostramos el arreglo ordenadop
print("Arreglo ordenado", ordenBurbuja)





