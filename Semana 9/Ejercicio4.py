
salario = [0,0,0,0,0,0,0]

for dia in range(7):
    salario[dia] = int(input("Salario del dia: "))

print("La semana completa: ", salario)
print("El total: ", sum(salario))
print("El minimo dia es: ", min(salario))


