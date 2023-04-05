#se crea la matriz de 5 notas por cada estudiante y en total son 4 estudiantes
calificacionesFinales = [[0 for nota in range(6)] for estudiante in range(4)]

#Se le solicita al usuario ingresar las notas
#se recorren los estudiantes
for estudiante in range(4):
    print("Ingrese el nombre del estudaintes #", estudiante+1 ,": ")
    nombre = input()
    calificacionesFinales[estudiante][0] = nombre
    for calificacion in range(5):
        print("Ingrese la nota del estudiante: ", nombre,': ')
        nota = float(input())
        calificacion += 1
        calificacionesFinales[estudiante][calificacion] = nota


#Calificaciones antes del cambio
for calificacion in calificacionesFinales:
    print(calificacion)

for i in range(len(calificacionesFinales)):
    for j in range(len(calificacionesFinales[i])):
        nota = calificacionesFinales[i][j]
        if isinstance(nota, float):
            if nota >= 80 and nota <= 85:
                calificacionesFinales[i][j] += 2
            elif nota >= 86 and nota <= 90:
                calificacionesFinales[i][j] += 4
            elif nota >= 91 and nota <= 99:
                calificacionesFinales[i][j] += 5
            elif nota == 100:
                calificacionesFinales[i][j] += 10

print("Calificaciones actualizadas: \n")
#Calificaciones finales
for calificacion in calificacionesFinales:
    print(calificacion)