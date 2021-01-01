import random

def letra_random():
    letras_español = ['m','n','r','i','a','o abierta','u estirada','u','o']

    print(random.choice(letras_español))

def main():
    otra_vez = ''

    while otra_vez != 'no':
        print('Te mostrare una letra en español y tu debes escribirla en coreano')
        letra_random()

        otra_vez = input('¿Quieres que te muestre otra letra? (si/no)')
        if otra_vez == 'si':
            print('Adios!')
            break
        

if __name__ == "__main__":
    main()