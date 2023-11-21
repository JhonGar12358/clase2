# 5. Validación de paréntesis
# Escribe una función que tome una cadena que contiene paréntesis y verifique si están balanceados.


def cadena_parentesis_balanceado(cadena):
    pila = []
    parentesis = {'(': ')'}

    for c in cadena:
        if c in parentesis:
            pila.append(c)
        elif len(pila) == 0 or c != parentesis[pila.pop()]:
            return False
            
        
    return len(pila) == 0

entrada= input('Ingrese los parentesis: ')

cadena_parentesis_balanceado(entrada)

#FALTA
