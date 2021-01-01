import random

def menu():
    print("""
    Este programa creado en python te ayudará a estudiar coreano, generando
    letras aleatorias para que las escribas en papel e incluso (en un futuro)
    te preguntara ciertas letras y tu debes escribir la letra que según tú
    es la correcta

    Selecciona una opción (1, 2)
        1 - Letras random 
        2 - Preguntar letras
    """)

def letra_random():
    letras_español = ['m','n','r','i','a','o abierta','u estirada','u','o']

    print(random.choice(letras_español))

def main():
    otra_vez = ''
    opcion = ''
    
    menu()

    if opcion == '1':
        while otra_vez != 'no':
            print('Te mostrare una letra en español y tu debes escribirla en coreano')
            letra_random()

            otra_vez = input('¿Quieres que te muestre otra letra? (si/no)')
            if otra_vez == 'no':
                print('Adios!')
                break
    elif opcion == '2':
        print('Esta opcion esta en proceso, elige otra opcion')
        main()
    else:
        print('La opcion que elegiste no existe vuelve a intentarlo')
        main()


if __name__ == "__main__":
    main()