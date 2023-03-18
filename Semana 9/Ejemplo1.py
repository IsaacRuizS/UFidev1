# declaracion
nombres = {}
#Declara la variable de lecturra dentro del ciclo while
nombre = " "
#Declara el indice del arreglo
indice = 0

while nombre != "":
    nombre = input("Escriba su nombre: ")
    #crea un espacio en el arreglo cuando nombre no este vacio
    if(nombre != ""):
        nombres[indice] = nombre
        indice += 1
#recorre el arreglo por cada elemento
for n in nombres:
    print(n, nombres[n])





