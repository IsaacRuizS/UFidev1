num1 = int(input("Ingrese el numero uno: "))
num2 = int(input("Ingrese el numero dos: "))
num3 = int(input("Ingrese el numero tres: "))
num4 = int(input("Ingrese el numero cuatro: "))

if num1>num2 and num1>num3 and num1>num4:
    print("numero mayor: ", num1)
elif num2>num1 and num2>num3 and num2>num4:
    print("numero mayor: ", num2)
elif num3>num2 and num3>num3 and num3>num4:
    print("numero mayor: ", num3)
else:
    print("numero mayor: ", num4)

