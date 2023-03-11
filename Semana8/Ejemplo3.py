def sumar(a, b):
    resultado = a + b
    print("La suma es: ", resultado)

def resta(a, b):

    resultado = a - b
    print("La resta es: ", resultado)

def division(a, b):
    resultado = a / b
    print("La division es: ", resultado)

def multiplicacion(a, b):
    resultado = a * b
    print("La multiplicacion es: ", resultado)


a = int(input("Primer valor: "))
b = int(input("Segundo valor: "))
sumar(a, b)
resta(a, b)
division(a, b)
multiplicacion(a, b)