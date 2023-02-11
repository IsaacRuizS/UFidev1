salario = float(input("Digite el salario del colaborador: "))
categoria = int(input(" 1. 10%\n 2. 12% \n 3. 15% \n 4. 20% \n Inserte la categoria: "))

if categoria == 1:
    aumento = salario*0.10
    salario += aumento
else:
    if categoria == 2:
        aumento = salario*0.12
        salario += aumento
    else:
        if categoria == 3:
            aumento = salario*0.15
            salario += aumento
        else:
            aumento = salario*0.20
            salario += aumento

print("El salario total es: $", salario)