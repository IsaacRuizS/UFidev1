personas = []
numero = 1

for i in range(5):
    i = int(input("Ingrese la edad de la persona numero " + str(numero)+ ": "))
    personas.append(i)
    numero +=1

resultado = sum(personas)/len(personas)
print(resultado)