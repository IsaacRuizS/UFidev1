cantidad = int(input("Digite la cantidad de articulos: "))
precio = float(input("Digite el total del precio de la compra: "))

if cantidad >= 12:
    descuento = precio * 0.20
    precio -= descuento
    print("El total con descuento de 20% es de:", precio)
else:
    print("Total sin descuento es de: ", precio)