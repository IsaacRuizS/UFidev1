#zona de funciones

#convertir binario no retorna e imprime resultado
def binario(n):
    resultado = bin(n)
    print(n, "En binario es", resultado[2:])
#convertir a octar retornando un valor
def octal(n):
    resultado = oct(n)
    return resultado
def hexadecimal(n):
    resultado = hex(n)
    return resultado

def potencia(base, exponente):
    return base ** exponente

print("Bienvenido al programa")
numero = int(input("Digite un numero entero: "))
binario(numero)
resultado = octal(numero)
print("numero en octal es: ", resultado[2:])
print("numero en hexadecimal es: ", hexadecimal(numero)[2:])

exponente= int(input("Digite el exponente"))
print("El numero elevado al exponente es: ", potencia(numero, exponente))


