edadLuis = int(input("Digite la edad de Luis: "))
edadPredro = (input("Digite la edad de Pedro: "))
#almacenamos la edad de luis en una variable tempora
temp = edadLuis
#intercambiamos las edades
edadLuis = edadPredro
edadPredro = temp
print("Edad de luis: ", edadLuis, "\n" + "Edad pedro: ", edadPredro)

