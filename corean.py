import random

def letra_random():
    letras_español = ['m','n','r','i','a','o abierta','u estirada','u','o']

    for i in letras_español:
        print(random.choice(letras_español))

def main():
    otra_vez = ''

    while otra_vez != 'si':
        print('Te mostrare una letra en español y tu debes escribirla en coreano')
        letra_random()

        otra_vez = input('¿Quieres que te muestre otra letra? (si/no)')
        

if __name__ == "__main__":
    main()