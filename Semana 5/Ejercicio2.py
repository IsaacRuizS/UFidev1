notaMayor = 0
notaMenor = 100
cantidadReprobados = 0
cantidadApobados = 0
nota = 0
#ciclo hasta que la nota no este en el rango
while nota >= 0 and nota< 100:
    nota = int(input("Digite la nota del estudiante"))
    if nota < 0 or nota > 100:
        break
    #Calcula la cantidad de reprobados y aprobaos
    if nota >= 70:
        cantidadApobados+=1
    else:
        cantidadReprobados+=1
    if nota > notaMayor:
        notaMayor = nota
    if nota < notaMenor:
        notaMenor = nota
print("Nota mayor ", notaMayor, "\n Nota Menor: ", notaMenor, "\n Aprobados: ", cantidadApobados, "\n Reprobados: ", cantidadReprobados)
