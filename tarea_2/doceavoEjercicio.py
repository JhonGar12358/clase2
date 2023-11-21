def primo(numero):
    

    if numero > 1:
        es_primo= True
        for i in range (2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break

    if es_primo and numero > 1:
        print(f"{numero} es un numero primo.")
    else:
        print(f"{numero} no es un numero primo")


primo(3)