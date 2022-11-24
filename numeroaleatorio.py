#Importar la libreria numero aleatroio.
import random

#Declarar las variables.
numero_pc = random.randint(1,10) #Variable con numero aleatorio con rango 1 a 10.
vidas = 0 #Vidas comienzan en 0(Contador para salir del ciclo).
jugando = True


# Funcion para Solicitar numero al usuario y verificar si es valido
def pedir_num():
    es_valido = False
    numeros = [1,2,3,4,5,6,7,8,9,10]

    while not es_valido:
        num_elegido = int(input("Elige un Numero del 1 al 10: "))
        if num_elegido in numeros:
            es_valido = True
        else:
            print("No has elegido un numero correcto, vuelve a ingresarlo")

    return num_elegido

#Imprimir el siguiente texto.
print("\t\tADIVINA UN NUMERO DEL 1 AL 10")

#Comienzo del ciclo.
while jugando:      
        vidas += 1
        if vidas <= 3: 
            numero_jugador = pedir_num()
            if numero_jugador >= 11: #Condicion para validar que el usuario no ingrese un numero mayor a 11 y no le reste vidas.
                print("Dato incorrecto")
                vidas = 0
            if numero_jugador == numero_pc: #Compara si el numero del usuario es igual al que la maquina genero, y si es asi el usuario gana, y le dice las vidas que necesito para ganar.
                print("\t\tHas acertado. Has necesitado", vidas, "vidas.")
                jugando = False
            elif numero_jugador > numero_pc: #Comapara si el numero del usuario es mayor al numero de la maquina, si es mayor le advierte que el numero es muy alto y las vidas que lleva.
                print("\t\tDemasiado alto. Llevas", vidas, "vidas.")
            elif numero_jugador < numero_pc: #Comapara si el numero del usuario es menor al numero de la maquina, si es menor le advierte que el numero es muy bajo y las vidas que lleva.
                print("\t\tDemasiado bajo. Llevas", vidas, "vidas.")

        else:
            print("\t\tSe te acabaron las vidas. Has perdido.") #En caso de que no se cumpla ninguna condicion, y las 3 vidas se gasten, el jugador pierde.
            jugando = False 


print("\t\tPresiona enter para salir...") #Detalle para que el programa no se cierre de asi nomas.
k=input() #Detalle para que el programa no se cierre de asi nomas.