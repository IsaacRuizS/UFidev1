#Parte 2

#Se inician las variables para ingresar al while y para sumas la cadenas y luego mostrarlas
numeroRecorridos = 1
mostrarCadena = ""

#Se realiza un ciclo que se realizara mientras el numero sea diferente de 0
while numeroRecorridos != 0:
    numeroRecorridos = int(input("ingrese un numero para recorrer: "))
    #Se recorre la cantidad de veces que el usuario indico
    for indice in range(0,numeroRecorridos):
        #se suma la cadena
        mostrarCadena += "$"
    #se muestra la cadena y se deja como vacia para luego volver a utilizarla y que no sume caracteres
    print(mostrarCadena)
    mostrarCadena = ""