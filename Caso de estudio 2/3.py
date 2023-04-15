# Seleccionar aleatoriamente una esquina de la matriz y marcarla como "marcada"
esquina = [(1, 1), (1, 5), (5, 1), (5, 5)]
selecion = random.choice(esquina)
# Se inicia el Bingo en donde se marca el cartón con las esquinas
print("Inicio Bingo")
for iterador in bingo:
    print(iterador)
print("--------------")
print("Comanzar a marcar esquinas")

# Se enumera numeros aleatorios sin reepeticion del 1 al 76
resultado = random.randrange(1, 76)
primeraEzquina = False
segundaEzquina = False
terceraEzquina = False
cuartaEzquina = False
#

esquina = [(1, 1), (1, 5), (5, 1), (5, 5)]
selecion = random.choice(esquina)
# bingo[selecion[0]][selecion[1]] = 'FREE'

# Imprimir el cartón de Bingo
for row in bingo:
    print(row)

# Repetir hasta que las cuatro esquinas estén marcadas
while True:
    tombola = []
    # Generar un número aleatorio del 1 al 75
    for iterador in range(1, 76):
        tombola.append(iterador)
    numeros = random.choice(tombola)
    tombola.remove(numeros)

    # Buscar el número en la columna correspondiente
    if numeros in Bnumeros:
        rowIndex = Bnumeros.index(numeros) + 1
        colIndex = 1
    elif numeros in Inumeros:
        rowIndex = Inumeros.index(numeros) + 1
        colIndex = 2
    elif numeros in Nnumeros:
        rowIndex = Nnumeros.index(numeros) + 1
        colIndex = 3
    elif numeros in Gnumeros:
        rowIndex = Gnumeros.index(numeros) + 1
        colIndex = 4
    elif numeros in Onumeros:
        rowIndex = Onumeros.index(numeros) + 1
        colIndex = 5
    else:
        continue