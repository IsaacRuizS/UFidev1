salario = float(input("Digite su salario: "))

if salario > 1000:
    incremento = salario * 0.15
    salario += incremento
    print("Su salario es de: $", salario, " con el incremento de 15%")
else:
    incremento = salario * 0.20
    salario += incremento
    print("Su salario es de: $", salario, " con el incremento de 20%")
