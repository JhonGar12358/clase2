# 8. Comprobación de palíndromos
# Escribe una función que verifique si una palabra dada es un palíndromo.


def palíndromo(word):
    palabra = []
    palabra = word 
    palabrare = ""

    for i in palabra:
        palabrare = i + palabrare
    
    print(palabrare)

    if palabrare == word:
        print('La palabra es palíndroma ')
    else:
        print('La palabra no es palíndroma ')

palíndromo('todavia')