# Escribe una función que tome una lista y devuelva un diccionario que muestre la frecuencia de cada elemento en la lista.
def frequency(array):
    cadenaPalabras = array
    

    listaPalabras = cadenaPalabras.split()

    frecuenciaPalab = []
    for w in listaPalabras:
        frecuenciaPalab.append(listaPalabras.count(w))

    print("Cadena\n" + cadenaPalabras +"\n")
    print("Lista\n" + str(listaPalabras) + "\n")
    print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
    print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))

variable = "el perro estaba jugando con otro perro mietras la niña jugaba con su perro de juguete"
frequency(variable)