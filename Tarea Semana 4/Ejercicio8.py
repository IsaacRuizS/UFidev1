horasTrabajadas = float(input("Ingrese las horas semanales trabajas: "))
precio = float(input("Ingrese el precio que se le paga por hora: "))

salarioSemanal = horasTrabajadas * precio
salarioMensual = salarioSemanal * 4.2

cargasSociales = salarioMensual * 0.105

salarioMensual -= cargasSociales
asociacion = salarioMensual * 0.05
salarioMensual -= asociacion

print("El salario neto es de: ", salarioMensual)

