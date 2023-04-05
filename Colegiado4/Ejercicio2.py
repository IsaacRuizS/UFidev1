continuar = True
def AgregarEstudiantes(nombre, calificacion):
    if calificacion < 0 or calificacion > 100:
        print("Error: la calificación debe estar entre 0 y 100")
        return

    categoria = ""
    if calificacion >= 80 and calificacion <= 90:
        categoria = "C"
    elif calificacion >= 91 and calificacion <= 95:
        categoria = "B"
    elif calificacion >= 96 and calificacion <= 100:
        categoria = "A"
    else:
        print("Error: la calificación debe estar entre 0 y 100")
        return

    with open("estudiantes.txt", "a") as archivo:
        archivo.write(nombre + "," + str(calificacion) + "," + categoria + "\n")


def MostrarEstudiantes():
    with open("estudiantes.txt", "r") as archivo:
        for linea in archivo:
            campos = linea.strip().split(",")
            nombre = campos[0]
            calificacion = campos[1]
            categoria = campos[2]
            print("Nombre: ", nombre)
            print("Calificación: ", calificacion)
            print("Categoría: ", categoria)
            print("\n")


while continuar != False:
    nombre = input("ingrese el nombre del estudiante: ")
    calificacion = float(input("ingrese la calificacion: "))
    AgregarEstudiantes(nombre, calificacion)
    solicitaContinuar = input("ingrese 1 si desea ingresar otro estudiante, si no, ingrese cualquier dato")
    if solicitaContinuar == "1":
        continuar = True
    else:
        continuar = False

MostrarEstudiantes()
