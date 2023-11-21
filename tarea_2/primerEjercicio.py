# 1. Suma de elementos en una lista
# Escribe una función que reciba una lista de números y devuelva la suma de todos los elementos.


def sum(list):
    sumaElem = 0

    for nota in list:
        sumaElem  += nota
    print(sumaElem)

list = []
cantNum = int(input('Cuantos numeros desea ingresar?: '))

for i in range (cantNum):
    x = int(input('Escribre un numero: '))
    list.append(x)
sum(list)