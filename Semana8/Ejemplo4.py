def sumar(a, b):
    resultado = a + b
    return resultado

def resta(a, b):

    resultado = a - b
    return resultado

def division(a, b):
    resultado = a / b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado


a = int(input("Primer valor: "))
b = int(input("Segundo valor: "))
sumar(a, b)
resta(a, b)
division(a, b)
multiplicacion(a, b)