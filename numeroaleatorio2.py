import random

numero = random.randint(1,10)
intentos = 0

jugando = True
print("ADIVINA UN NUMERO DEL 1 AL 10")

while jugando:
    intentos += 1
    if intentos <= 3:
        eleccion = int(input("Dime un numero: "))
        if eleccion == numero:
            print("Has acertado. Has necesitado", intentos, "intentos.")
            jugando = False
        elif eleccion > numero:
            print("Demasiado alto. Llevas", intentos, "intentos.")
        elif eleccion < numero:
            print("Demasiado bajo. Llevas", intentos, "intentos.")
    else:
        print("Se te acabaron los intentos. Has perdido.")
        jugando = False
