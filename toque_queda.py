#Trabajo de toque y queda
# Con Sofia Castro, Anibal Muñoz y Victor Camero
import random

contador = 1
while True:
    if contador == 1:
        confirmar_jugar = input("S si desea jugar y N si no quiere jugar:")
    else:
        confirmar_jugar = input("Si quieres volver a jugar presione S y si quiere dejar de jugar presione N: ")
    if confirmar_jugar.upper() == "S":
        print("Vamos a jugar")
        a = random.randrange(10)
        b = random.randrange(10)
        c = random.randrange(10)
        d = random.randrange(10)
        if a != b and a != c and a != d and b != c and b != d and c != d:
            print(a, b, c, d)
        else:
            while a == b or a == c or a == d or b == c or b == d or c == d:
                a = random.randrange(10)
                b = random.randrange(10)
                c = random.randrange(10)
                d = random.randrange(10)
            print(a, b, c, d)

        turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
        for partidas in range(turnos_a_jugar):
            turno = partidas + 1
            intento = int(input(f"{turno}) ingrese los numeros: "))

    elif confirmar_jugar.upper() == "N":
        print("Espero que quieras volver a jugar.")
        exit()
    else:
        print("Esta opcion no esta permitida")

    contador += 1