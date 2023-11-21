#PRIMER EJERCICIO

# asc = 0
# des = 11

# while asc < 10:
#     asc += 1
#     des -= 1
#     print(asc, '//', des)

#SEGUNDO EJERCICIO

# import random
# aleatorio = random.randint(1, 100)

# print(aleatorio)

# adivina = 0

# while adivina != aleatorio:
#     if adivina == 0:
#         print('Inicia el juego')
#     elif adivina < aleatorio:
#         print('demasiado bajo')
#     else:
#         print('demasiado alto')
#     adivina = int(input('ingresa el numero'))

# TERCER EJERCICIO

# num= int(input('Escribe el numero a multiplicar: '))

# for u in range(1,11):
     
#      print(num,'x',u,'=',(num*u))

# CUARTO EJERCICIO 
# Pide al usuario que ingrese un número entero y utiliza un bucle "for" para sumar todos los números pares desde 2 hasta el número ingresado. Muestra el resultado.


# entero = int(input('ingresa un numero entero: '))
# contador = 0

# for y in range (2, entero + 1, 2):
#     contador += y

# print(contador)




    
#QUINTO EJERCICIO
# n = 5

# for i in range(1, n + 1):
#     for j in range(i):
#         print('* ', end='')
#     print()






    


#SEXTO EJERCICIO

# number = int(input('ingresa un numero : '))
# contador= 0
# if number > 0:
#     for i in range (2, number+1, 2):
#         contador += i
#     print(contador)  
# else:
#     print("El valor ingresado es menor o igual a cero.") 

    
# Crea un programa que solicite al usuario ingresar una cadena y luego cuente 
# la cantidad de vocales (a, e, i, o, u) en la cadena utilizando un bucle "while" y una estructura condicional "if".


# SEPTIMO EJERCICIO 



# sum = 0
# text= input("ingresa una frase: ")
# indice = 0
# while indice < len(text):
#     caracter = text[indice]
#     if caracter in "aeiouAEIOU":

#         sum += 1
#     indice += 1       
# print("las vocales sumadas son: ",sum) 

#OCTAVO EJERCICIO

# Números primos con "for", "if" y "else"
# Escribe un programa que solicite al usuario ingresar un número y determine si es un número primo o no utilizando un bucle "for", 
# una estructura condicional "if" y "else". Muestra un mensaje apropiado.


# numero = int(input('Ingrese un numero: '))

# es_primo= True

# if numero > 1:
#     for i in range (2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             es_primo = False
#             break

# if es_primo and numero > 1:
#     print(f"{numero} es un numero primo.")
# else:
#     print(f"{numero} no es un numero primo")

#NOVENO EJERCICIO

# import random 
# aleatorio = random.randint(1, 100)
# adivina = 0
# while adivina != aleatorio:
    
#     if adivina == 0:
#         print('Inicia el juego')
#     elif adivina < aleatorio and adivina <= 100:
#         print('demasiado bajo')
#     else:
#         print('demasiado alto')
#     adivina = int(input('ingresa el numero: '))





#DECIMO EJERCICIO

# numero = int(input("Ingrese un numero: "))
    
# if numero % 2 == 0:
#     print("*"*numero)
# else:
#     for i in range(numero):
#         print("*" * (i+ 1))

       




    