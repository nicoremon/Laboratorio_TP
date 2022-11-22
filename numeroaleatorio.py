import random

numero_pc = random.randint(1,10)
vidas = 0
jugando = True




    

print("\t\tADIVINA UN NUMERO DEL 1 AL 10")

while jugando:      
        vidas += 1
        if vidas <= 3:
            numero_jugador = int(input("Dime un numero: "))   
            if numero_jugador >= 11:
                print("Dato incorrecto")
                vidas = 0
            if numero_jugador == numero_pc:
                print("\t\tHas acertado. Has necesitado", vidas, "vidas.")
                jugando = False
            elif numero_jugador > numero_pc and numero_jugador <= 10:
                print("\t\tDemasiado alto. Llevas", vidas, "vidas.")
            elif numero_jugador < numero_pc:
                print("\t\tDemasiado bajo. Llevas", vidas, "vidas.")

        else:
            print("\t\tSe te acabaron las vidas. Has perdido.")
            jugando = False 





        
print("\t\tPresiona enter para salir...")
k=input()