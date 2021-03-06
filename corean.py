import random

def menu():
    print("""
    Este programa creado en python te ayudará a estudiar coreano, generando
    letras aleatorias para que las escribas en papel e incluso (en un futuro)
    te preguntara ciertas letras y tu debes escribir la letra que según tú
    es la correcta

    Selecciona una opción (1, 2, 3)
        1 - Letras random 
        2 - Preguntar letras
        3 - Salir
    """)

def letra_random():
    letras_español = ['m','n','r','i','a','o abierta','u estirada','u','o', 
    'p con poco aire', 't con poco aire', 'k con poco aire', 's con poco aire', 'ch',
    'ia', 'iu', 'io', 'io abierta', 'ui estirada', 'p con mucho aire', 
    't con mucho aire', 'k con mucho aire', 'h', 'ch con mucho aire', 'e abierta', 'e cerrada',
    'ui', 'uo', 'ua']

    print(random.choice(letras_español))

def main():
    opcion = ''
    
    menu()
    opcion = input('Introduce una opcion del menu: ')
    if opcion == '1':
        otra_vez = ''
        while otra_vez != 'no':
            print('Te mostrare una letra en español y tu debes escribirla en coreano')
            letra_random()

            otra_vez = input('¿Quieres que te muestre otra letra? (si/no)')
            if otra_vez == 'no':
                main()
                break
    elif opcion == '2':
        print('Esta opcion esta en proceso, elige otra opcion')
        main()
    elif opcion == '3':
        print('Adios!')
    else:
        print('La opcion que elegiste no existe vuelve a intentarlo')
        main()


if __name__ == "__main__":
    main()