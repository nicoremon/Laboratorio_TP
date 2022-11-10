# Importo libreria choice para seleccion un elemento al azar del array de palabras
from random import choice
# Juego Ahorcado

# Variables
palabras = ['juego', 'ahorcado', 'utn', 'programacion', 'villamaria', "cordoba"]
intentos = 6
aciertos = 0
juego_terminado = False
letras_correctas = []
letras_erroneas = []
palabra_elegida = elegir_palabra(palabras)

# Sorteo para obtener palabra para jugar
def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

# Funcion para solicitar letra y corroborar que sea correcta
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida

# Inicio Juego Ahorcado
print("--------------------------------")
print("Bienvenido al Juego del Ahorcado")
print("--------------------------------")
print("Usted contara con 6 intentos para adivinar la palabra secreta")
print("--------------------------------")

# Informar Longitud de palabra secreta
# Mostrar por pantalla la cantidad de _ segun la longitud de la palabra
len_palabra_elegida = len(palabra_elegida)
print(f"La longitud de la palabra secreta es de {len_palabra_elegida} caracteres")
print("_ "*len_palabra_elegida)
guiones_ = "_ " * len_palabra_elegida


# El juego funciona mientras el usuario no pierda
while juego_terminado == False:
        
    # Solicitar a usuario letra a adivinar..
    #letra_consulta(letra)
    letra = pedir_letra()

    # Comprobar si la letra se encuentra dentro de la palabra secreta
    if letra in palabra_elegida:
        posicion = palabra_elegida.find(letra)
        #fragmento = palabra_secreta[posicion]
        #palabra = palabra.replace(fragmento in posicion)
        print(f"La letra se encuentra dentro de la palabra secreta en la posicion {posicion}")
        #print(fragmento) # Para hacer esto tengo que corroborar donde se encuentra y si se repite
        
    # Ver de convertir esto en funciones y que valla llamando segun cantidad de vidas restantes    
    else:
        intentos -= 1
        if intentos == 5:
            print('''
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            ''')

            letras_erroneas.append(letra)
            print("La letra ingresada no se encuentra en la palabra")
            print(f"Letras erroneas ingresadas: {letras_erroneas}, le quedan {intentos} intentos restantes")

        elif intentos == 4:
            print('''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            ''')

            letras_erroneas.append(letra)
            print("La letra ingresada no se encuentra en la palabra")
            print(f"Letras erroneas ingresadas: {letras_erroneas}, le quedan {intentos} intentos restantes")

        elif intentos == 3:
            print('''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            ''')

            letras_erroneas.append(letra)
            print("La letra ingresada no se encuentra en la palabra")
            print(f"Letras erroneas ingresadas: {letras_erroneas}, le quedan {intentos} intentos restantes")

        elif intentos == 2:
            print('''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========
            ''')

            letras_erroneas.append(letra)
            print("La letra ingresada no se encuentra en la palabra")
            print(f"Letras erroneas ingresadas: {letras_erroneas}, le quedan {intentos} intentos restantes")

        elif intentos == 1:
            print('''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========
            ''')

            letras_erroneas.append(letra)
            print("La letra ingresada no se encuentra en la palabra")
            print(f"Letras erroneas ingresadas: {letras_erroneas}, le quedan {intentos} intentos restantes")

        elif intentos == 0:
            print('''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========
            ''')
            
            letras_erroneas.append(letra)
            print("La letra ingresada no se encuentra en la palabra. Usted Perdio")
            print(f"Letras erroneas ingresadas: {letras_erroneas}, le quedan {intentos} intentos restantes")
            juego_terminado = True
            
    # Volver a jugar ? Resolver esto
    fin = input("Usted perdio el Juego :( Quiere jugar de nuevo? s/n: ")
                       
    if fin == "s":
        intentos = 6
        juego_terminado = False
        continue
    else:
        print("Gracias por jugar")
        juego_terminado = True
        break


            

