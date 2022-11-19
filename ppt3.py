import random

#Para que el juego quede mas personalizado le pedimos al jugador su nombre
nombre = input("Hola vamos a jugar a piedra (1), papel (2) o tijeras (3), mi nombre es Pc. ¿Y tú, cómo te  llamas ? ")
print("Encantado de conocerte " + nombre)
print("Empezamos")

#Agregamos sumador para medir quien va ganado
ganando = 0
perdiendo = 0
Maxju = 0
numvalido = 1,2,3

#elegir eleatorio -random- elegir jugador.
# Tambien se puede usar random.randrange (1, 4) el 4 no es considerado.
while Maxju < 3:
    Maxju = Maxju +1
    aleatorio = random.randint(1, 3)
    Pc = ""

    #el usuario debe elegir entre los 3 numero. 
    #si se coloca un numero distinto se le pedira nuevamente una opcion
    opcion = int(input("Elige tu opción "))
    if opcion in numvalido:
      
    else: 
        opcion = int(input("Elige tu opción "))


    #aqui comienza el recorrido de la eleccion del usuario
    if opcion == 1:
        Usuario = "Piedra"
    elif opcion == 2:
        Usuario = "Papel"
    elif opcion == 3:
        Usuario = "Tijeras"
    print("Elejiste: ", Usuario)

    if aleatorio == 1:
        Pc = "Piedra"
    elif aleatorio == 2:
        Pc = "Papel"
    elif aleatorio == 3:
        Pc = "Tijeras"
    print("Yo elegi: ", Pc)

  
   #compara elección y anuncia quien gano. Ademas de ir sumando las ganadas o perdidas.
    if Pc == "Piedra" and Usuario == "Papel":
        print("Usted gana") 
        ganando = ganando +1
        print(ganando)
    elif Pc == "Papel" and Usuario == "Tijeras":
        print("Usted gana")
        ganando = ganando +1
        print(ganando)
    elif Pc == "Tijeras" and Usuario == "Piedra":
        print("Usted gana")
        ganando = ganando +1
        print(ganando)
    if Pc == "Piedra" and Usuario == "Tijeras":
        print("Usted pierde")
        perdiendo = perdiendo +1
        print(perdiendo)
    elif Pc == "Tijeras" and Usuario == "Papel":
        print("Usted pierde")
        perdiendo = perdiendo +1
        print(perdiendo)
    elif Pc == "Papel" and Usuario == "Piedra":
        print("Usted pierde")
        perdiendo = perdiendo +1
        print(perdiendo)
    elif Pc == Usuario:
     print("Empate -no suma-")


     
play_again = input("Revancha? (s/n): ")
if play_again.lower() != "s":
    break