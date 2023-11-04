#PRIMER EJERCICIO

# asc = 0
# des = 11

# while asc < 10:
#     asc += 1
#     des -= 1
#     print(asc, '//', des)

#SEGUNDO EJERCICIO

import random
aleatorio = random.randint(1, 100)

print(aleatorio)

adivina = 0

while adivina != aleatorio:
    if adivina == 0:
        print('Inicia el juego')
    elif adivina < aleatorio:
        print('demasiado bajo')
    else:
        print('demasiado alto')
    adivina = int(input('ingresa el numero'))



    