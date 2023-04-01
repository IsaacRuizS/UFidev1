def saludar(nombre):
    print("Bienvenido a python ", nombre)

usuario = input("Ingrese el nombre del usuario: ")
#saludar(usuario)

#funcion que retorna el articulo por comprar
def solicitarArticulo(posicion):
    print("escriba el nombre del articulo #", posicion+1, ":",end="")
    resultado = input()
    return resultado

#funcion que imprime los articulos comprados
def listarCompras(comprador, listaCompras):
    print("La lista de compras de ", comprador, "es: ")
    largo = len(listaCompras)
    for posicion in range(largo):
        print("Articulo numero", posicion+1, ":", listaCompras[posicion])


#declara una lista unidimensional
listaCompras = {}
#Declara la variable de control para los articulos que se compraran
articulo = " "
#inidce
contador = 0
#recorre el ciclo hasta que articulo no sea vacio
while articulo != "":
    # solicita al usuario el articulo por comprar
    articulo= solicitarArticulo(contador)
    #si no es vacio lo inserta en la lista de compras
    if articulo != "":
        listaCompras[contador] = articulo
        #aumenta el contador para la siguinete iteracion
        contador +=1
#ejecuta la funcion para mostrar la lista
listarCompras(usuario,listaCompras)