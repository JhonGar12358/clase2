
# PRIMER EJERCICIO

num = int(input("Escribe un numero: "))

if num % 2= 0:
    print('es par')
else:
    print('es impar')

# SEGUNDO EJERCICIO

edad= int(input('Escribe tu edad: '))

if edad < 18:
    print('eres menor de edad')
elif edad >= 18 and edad <= 65:
    print('eres mayor de edad')
else:
    print('eres un adulto mayor')

# TERCER EJERCICIO

precio = int(input('ingrese el precio del producto: '))
edad = int(input('Ingrese su edad: '))

if edad < 18:
    descuentoMen = (precio*10)/100
    total= print('su descuento es del 10% y el total a pagar es:', precio-descuentoMen)
elif edad >= 65:
    descuentoMay= (precio*15)/100 
    total= print('su descuento es del 15% y el total a pagar es:' , precio-descuentoMay)
elif edad >= 18 and edad <= 65:
    total= 'no tienes descuento'
    print(total)




# CUARTO EJERCICIO

puntuacion = int(input('Ingrese la puntuación: '))

if puntuacion >= 90 and puntuacion<= 100:
    print('"A" (sobresaliente)')
elif puntuacion >= 80 and puntuacion< 90:
    print('"B" (bueno)')
elif puntuacion >= 70 and puntuacion<= 79:
    print('"C" (satisfactorio)')
elif puntuacion >= 60 and puntuacion<= 69:
    print('"D" (necesita mejorar)') 
elif puntuacion < 60:
    print('"F" (reprobado)')

# QUINTO EJERCICIO

salario = int(input('ingrese su salario anual: '))

if salario <= 10000:
    paga= print('no paga impuesto')

elif salario > 10000 and salario <= 50000:
    impuesto = (salario*10)/100
    paga = print('su impuesto es el 10% de su salario, debe pagar:',  impuesto)

elif salario > 50000 and salario <= 100000:
    impuesto = (salario*20)/100
    paga = print('su impuesto es el 20% de su salario, debe pagar:', impuesto)

elif salario > 100000:
    impuesto = (salario*30/100)
    paga = print('su impuesto es el 30% de su salario, debe pagar:',  impuesto)
    
