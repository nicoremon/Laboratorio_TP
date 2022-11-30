#Importar la libreria numero aleatroio.
import random

def adivinaNumero():

#Declarar las variables.
    numero_pc = random.randint(1,10) #Variable con numero aleatorio con rango 1 a 10.
    vidas = 0 #Vidas comienzan en 0(Contador para salir del ciclo).
    jugando = True

    # Funcion para Solicitar numero al usuario y verificar si es valido
    def pedir_num():
        while True:
            num_elegido = 0
            numeros = [1,2,3,4,5,6,7,8,9,10]
            try:
                num_elegido = int(input("Ingresa la opcion: "))
            except ValueError:
                print("Debes escribir un número entre 1 y 10.")
                continue

            if num_elegido not in numeros:
                print("Debes escribir un número entre 1 y 10.")
                continue
            else:
                break

        return num_elegido

    #Imprimir el siguiente texto.   
    print(" ")
    print("\t\tADIVINA UN NUMERO DEL 1 AL 10")
    print(" ")

    #Comienzo del ciclo.
    while jugando:      
            
            vidas += 1
            if vidas <= 3:
                num_elegido = pedir_num()   
                if int(num_elegido) == numero_pc: #Compara si el numero del usuario es igual al que la maquina genero, y si es asi el usuario gana, y le dice las vidas que necesito para ganar.
                    print("\t\tHas acertado. Has necesitado", vidas, "vidas.")
                    jugando = False
                elif int(num_elegido) > numero_pc: #Comapara si el numero del usuario es mayor al numero de la maquina, si es mayor le advierte que el numero es muy alto y las vidas que lleva.
                    print("\t\tDemasiado alto. Llevas", vidas, "vidas.")
                elif int(num_elegido) < numero_pc: #Comapara si el numero del usuario es menor al numero de la maquina, si es menor le advierte que el numero es muy bajo y las vidas que lleva.
                    print("\t\tDemasiado bajo. Llevas", vidas, "vidas.")

            else:
                print("\t\tSe te acabaron las vidas. Has perdido.") #En caso de que no se cumpla ninguna condicion, y las 3 vidas se gasten, el jugador pierde.
                jugando = False 


    print(" ")
    jugar_de_nuevo = input("Quieres volver a Jugar ? (s/n): ") #Consula al usuario si quiere volver a jugar a adivina un numero.
    if jugar_de_nuevo == 's':
        adivinaNumero() 
    else:
        print(" ")        
        print("\t\tPresiona enter para volver al menu...") #Detalle para que el programa no se cierre de asi nomas.
        k=input() #Detalle para que el programa no se cierre de asi nomas.