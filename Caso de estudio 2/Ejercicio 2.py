
import random

# Generar los números aleatorios para cada columna
Bnumeros = random.sample(range(1, 16), 5)
Inumeros = random.sample(range(16, 31), 5)
Nnumeros = random.sample(range(31, 46), 5)
Gnumeros = random.sample(range(46, 61), 5)
Onumeros = random.sample(range(61, 76), 5)

# Crear la matriz del cartón de Bingo
bingo = [
    ['B', 'I', 'N', 'G', 'O'],
    [Bnumeros[0], Inumeros[0], Nnumeros[0], Gnumeros[0], Onumeros[0]],
    [Bnumeros[1], Inumeros[1], Nnumeros[1], Gnumeros[1], Onumeros[1]],
    [Bnumeros[2], Inumeros[2], Nnumeros[2], Gnumeros[2], Onumeros[2]],
    [Bnumeros[3], Inumeros[3], Nnumeros[3], Gnumeros[3], Onumeros[3]],
    [Bnumeros[4], Inumeros[4], Nnumeros[4], Gnumeros[4], Onumeros[4]]]

# Seleccionar aleatoriamente una esquina de la matriz y marcarla como "marcada"
esquina = [(1,1), (1,5), (5,1), (5,5)]
seleccion = random.choice(esquina)

print("Inicio Bingo")
for iterador in bingo:
    print(iterador)
print("--------------")
print("Comenzar a marcar esquinas")

tombola = []
for iterador in range(1, 76):
    tombola.append(iterador)

primeraEzquina = False
segundaEzquina = False
terceraEzquina = False
cuartaEzquina = False

bingoGanado = True
contador=0
# Crear una lista de números del 1 al 76

while bingoGanado:
    contador +=1
    resultado = random.choice(tombola)
    tombola.remove(resultado)
    if(resultado == bingo[1][0]):
        primeraEzquina= True
        bingo[1][0] = "x"
        for iterador in bingo:
            print(iterador)
        print(contador)
        print("--------------")
    elif(resultado == bingo[5][0]):
        segundaEzquina= True
        bingo[5][0] = "x"
        for iterador in bingo:
            print(iterador)
        print(contador)
        print("--------------")
    elif(resultado == bingo[1][4]):
        terceraEzquina= True
        bingo[1][4] = "x"
        for iterador in bingo:
            print(iterador)
        print(contador)
        print("--------------")
    elif(resultado == bingo[5][4]):
        cuartaEzquina= True
        bingo[5][4] = "x"
        for iterador in bingo:
            print(iterador)
        print(contador)
        print("--------------")

    if(primeraEzquina == True and segundaEzquina == True and terceraEzquina == True and cuartaEzquina == True):
        print("BINGOOO", contador, "Intentos")
        bingoGanado = False