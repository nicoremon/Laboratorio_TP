from ast import If
from operator import truediv
import random
numeroAleatorio = random.randint(1,10)

def intro():
    print("*"*40)
    print(" "*10,"ADIVINA EL NUMERO"," "*10)
    print("*"*40)

def juega():
    intentos = 0
    while True:
        numUsuario = int(input("Inserta un numero entre el 1 y el 10: "))
        if numUsuario > numeroAleatorio:
            intentos += 1
            print("El numero a acertar es mas pequeño, intentalo de nuevo.")
        elif intentos > 1:
            print("Perdiste")
            str("Desea volver a empezar ?")
            
        elif numUsuario < numeroAleatorio:
            intentos += 1
            print("El numero a acertar es mas grande, intentalo de nuevo.")        
        else:
            intentos += 1
            print(f"Felicidades, el numero era {numeroAleatorio} y lo lograste en {intentos}")
            break

intro()  
juega() 