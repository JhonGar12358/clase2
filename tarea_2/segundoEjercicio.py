# 2. Verificar paridad
# Escribe una función que tome un número como argumento y devuelva un mensaje indicando si es par o impar.


def indicar(num):
    if num % 2 == 0:
        print('es par')
    else:
        print('es impar')

num = int(input('Ingresa el numero: '))

indicar(num)




 