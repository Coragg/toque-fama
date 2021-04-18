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
        i=0
        t=0
        turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
        for partidas in range(turnos_a_jugar):
            turno = partidas + 1
            intento = input(f"{turno}) ingrese los numeros: ")
            if len(intento) == 4:
                print("Se acepta")
                if(str(a)==intento[0]):
                    i=i+1
                elif(str(a)==intento[1] or str(a)==intento[2] or str(a)==intento[3]):
                    t=t+1
                if(str(b)==intento[1]):
                    i=i+1
                elif(str(b)==intento[0] or str(b)==intento[2] or str(b)==intento[3]):
                    t=t+1
                if(str(c)==intento[2]):
                    i=i+1
                elif(str(c)==intento[0] or str(c)==intento[1] or str(c)==intento[3]):
                    t=t+1
                if(str(d)==intento[3]):
                    i=i+1
                elif(str(d)==intento[0] or str(d)==intento[1] or str(d)==intento[2]):
                    t=t+1
                if(i==0):
                    print("Fama=0")
                elif(i==1):
                    print("Fama=1")
                elif(i==2):
                    print("Fama=2")
                elif(i==3):
                    print("Fama=3")
                elif(i==4):
                    print("Fama=4 !!FELICIDADES GANASTE¡¡")
                    break
                if(t==0):
                    print("Toque=0")
                elif(t==1):
                    print("Toque=1")
                elif(t==2):
                    print("Toque=2")
                elif(t==3):
                    print("Toque=3")
                elif(t==4):
                    print("Toque=4")
                i=0
                t=0
            else:
                print("No se acepta")
                break
    elif confirmar_jugar.upper() == "N":
        print("Espero que quieras volver a jugar.")
        exit()
    else:
        print("Esta opcion no esta permitida")

    contador += 1