import random

def juego_adivinanza():
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    print("¡Bienvenido al juego de adivinanza!")
    print("Debes adivinar un número entre 1 y 100")
    print("¡intenta adivinarlo!")

    while not adivinado:
        # solicitar un número
        adivinanza = input("Introdusca un número del 1 al 100:")
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(f"¡Felicidades has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos.")
                adivinado = True
        else:
            print("Por favor Introduzca un numero válido entre 1 y 100")

juego_adivinanza()