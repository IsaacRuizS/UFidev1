#zona de funciones

#convertir binario no retorna e imprime resultado
def binario(n):
    resultado = bin(n)
    print(n, "En binario es", resultado)
#convertir a octar retornando un valor
def octal(n):
    resultado = oct(n)
    return resultado
def hexadecimal(n):
    resultado = hex(n)
    return resultado

def potencia(base, exponente):
    return base ** exponente
