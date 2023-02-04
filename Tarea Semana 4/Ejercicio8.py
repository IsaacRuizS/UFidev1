#Ejercicio 8
#Se toman las horas trabajadas y el precio a la que se le pagan
horasTrabajadas = int(input("Ingrese las horas semanales trabajas: "))
precio = float(input("Ingrese el precio que se le paga por hora: "))

#Se obtienen los salarios mensuales y semanales a 4.2 semanas
salarioSemanal = horasTrabajadas * precio
salarioMensual = salarioSemanal * 4.2

#se obtiene la cantidad de carga social que se debe de descontar
cargasSociales = salarioMensual * 0.105

#se descuentan las cargas sociales
salarioMensual -= cargasSociales
#se obtiene la cantidad de la asociacion que se debe de descontar
asociacion = salarioMensual * 0.05
#se descuenta el valor de la asociacion
salarioMensual -= asociacion
#se mueestra
print("El salario neto es de: ", salarioMensual)

