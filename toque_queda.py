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
            intento = input(f"{turno}) ingrese los numeros: ")
            if len(intento) == 4:
                print("Se acepta")
                if(str(a)==intento[0]):
                    print("F")
                elif(str(a)==intento[1] or str(a)==intento[2] or str(a)==intento[3]):
                    print("T")
                if(str(b)==intento[1]):
                    print("F")
                elif(str(b)==intento[0] or str(b)==intento[2] or str(b)==intento[3]):
                    print("F")
                if(str(c)==intento[2]):
                    print("F")
                elif(str(c)==intento[0] or str(c)==intento[1] or str(c)==intento[3]):
                    print("T")
                if(str(d)==intento[3]):
                    print("F")
                elif(str(d)==intento[0] or str(d)==intento[1] or str(d)==intento[2]):
                    print("T")
            else:
                print("No se acepta")

    elif confirmar_jugar.upper() == "N":
        print("Espero que quieras volver a jugar.")
        exit()
    else:
        print("Esta opcion no esta permitida")

    contador += 1