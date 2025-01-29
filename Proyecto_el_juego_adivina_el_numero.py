#Juego 'Adivina el numero'
from random import randint

intentos = 8
intentos_tomados = 0
numero_secreto = randint(1, 100) #Generamos el numero aleatorio

print("\U0001F522 Bienvenido al juego 'Adivina el número' \U0001F914 \n")
nombre_del_usuario = input("Ingresa tu nombre: ")
print(f"Hola \U0001F44B {nombre_del_usuario}, he pensado en un número entre el 1 al 100 y tienes 8 intentos para adivinar cual es. \U0001F92B \n"
      f"¿Podrás lograrlo? \U0001FAE2")

while intentos > 0:

    numero_elegido = int(input("Escoge un número: "))  #El usuario ingresa su numero

    if numero_elegido < 1 or numero_elegido > 100:
        intentos = intentos - 1
        intentos_tomados = intentos_tomados + 1
        print(f"INCORRECTO, ese número no está permitido. \U0001F635 Te quedan {intentos} intentos.")
    elif numero_elegido < numero_secreto:
        intentos = intentos - 1
        intentos_tomados = intentos_tomados + 1
        print(f"INCORRECTO, el número ingresado es menor al secreto. \U0001F90F Te quedan {intentos} intentos.")
    elif numero_elegido > numero_secreto:
        intentos = intentos - 1
        intentos_tomados = intentos_tomados + 1
        print(f"INCORRECTO. El número ingresado es mayor al número secreto. \U0001F90F Te quedan {intentos} intentos.")
    elif numero_elegido == numero_secreto:
        print(f"\U0001F973 Felicidades {nombre_del_usuario} \U0001F389, has adivinado el número secreto '{numero_secreto}'. \U0001F60E")
        print(f"Te ha tomado {intentos_tomados} intentos.")
        intentos = 0

if intentos_tomados == 8:
    print(f"El número secreto era {numero_secreto}.\n")

print("\U0001F47E GAME OVER \U0001F47E")