#Solicitamos los datos
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

#Se valida si a es el mayor
if a>b and a>c:
    # Se valida si luego de a, b es el mayor y se imprime el orden
    if b>c:
        print(a)
        print(b)
        print(c)
    # Si no, c es el mayor luego de a y se imprime
    else:
        print(a)
        print(c)
        print(b)
#Se valida si b es el mayor
elif b>a and b>c:
    # Se valida si luego de b, a es el mayor y se imprime el orden
    if a>c:
        print(b)
        print(a)
        print(c)
    # Si no, c es el mayor luego de b y se imprime
    else:
        print(b)
        print(c)
        print(a)
#Se valida si c es el mayor
elif c>a and c>b:
    # Se valida si luego de c, a es el mayor y se imprime el orden
    if a>b:
        print(c)
        print(a)
        print(b)
    # Si no, b es el mayor luego de c y se imprime
    else:
        print(c)
        print(b)
        print(a)