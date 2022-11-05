# Juego Ahorcado
# Variables
intentos = 6
#letra = ""
# Set de palabras secretas
palabras = {'juego', 'ahorcado', 'facultad', 'programacion'}
# Sorteo para obtener palabra para jugar
palabra_secreta = palabras.pop()
# Lista de letras erroneas introducidas por Jugador
letras_erroneas = []
# Funcion para solicitar letra a adivinar.
#def letra_consulta(Letra):
#    letra = input("Ingrese letra a adivinar: ")
#    return letra

# Inicio Juego Ahorcado
print("--------------------------------")
print("Bienvenido al Juego del Ahorcado")
print("--------------------------------")
print("Usted contara con 6 intentos para adivinar la palabra secreta")
print("--------------------------------")

# Informar Longitud de palabra secreta
# Mostrar por pantalla la cantidad de _ segun la longitud de la palabra
len_palabra_secreta = len(palabra_secreta)
print(f"La longitud de la palabra secreta es de {len_palabra_secreta} caracteres")
print("_ "*len_palabra_secreta)
guiones_ = "_ " * len_palabra_secreta

# Armando la palabra con replace en los _ por las letras adivinidas en su posicion
palabra = guiones_

# El juego funciona mientras el usuario cuente con intentos disponibles (partes del ahorcado = 6)
while intentos > 0:
        
    # Solicitar a usuario letra a adivinar..
    #letra_consulta(letra)
    letra = input("Ingrese letra a adivinar: ")

    # Comprobar si la letra se encuentra dentro de la palabra secreta
    if letra in palabra_secreta:
        posicion = palabra_secreta.find(letra)
        #fragmento = palabra_secreta[posicion]
        #palabra = palabra.replace(fragmento in posicion)
        print(f"La letra se encuentra dentro de la palabra secreta en la posicion {posicion}")
        #print(fragmento) # Para hacer esto tengo que corroborar donde se encuentra y si se repite
        
    # a este le tengo que poner un condicional que imprima x dibujo dependiendo de como esta el contador de intentos    
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
            print("La letra ingresada no se encuentra en la palabra")
            print(f"Letras erroneas ingresadas: {letras_erroneas}, le quedan {intentos} intentos restantes")
            
            # Volver a jugar ? Resolver esto
            fin = input("Usted perdio el Juego :( Quiere jugar de nuevo? s/n: ")
                        
            if fin == s:
                intentos = 6
                continue
            else:
                print("Gracias por jugar")
                break


            

