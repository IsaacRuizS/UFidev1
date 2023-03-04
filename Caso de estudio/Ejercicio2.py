#Primera parte, tercer ejercicio
#Se solicita la letra
letra = input("Ingrese una letra: ")

#Se realiza una condicion para validar si la letra es consonante o vocal sin importar si es mayuscula o minuscula.
if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" ):
    #Se imprime el resultado
    print("La letra ", letra, "que ingresaste es una vocal")
else:
    #Se imprime el resultado
    print("La letra ", letra, "que ingresaste es una consonante")