#Trabajo de toque y fama
# Con Sofia Castro, Anibal Muñoz y Victor Camero
import random
print("-----------------------------------------------------------------------")
print("Bienvenido al juego: toque y fama")
print("El objetivo del juego: el juego generara de manera aleatoria 4 numeros\n"
      "del cero al nueve, tu deber es encontrarlos con las siguientes pistas\n"
      "si tienes 1 toque encontraste 1 numero pero no en el lugar indicado\n"
      "si encontraste 1 fama encontraste 1 numero y en el lugar indicado\n"
      "si logras 4 famas, felicidades ganaste")
print("-----------------------------------------------------------------------")
contador = 1
ganadas= 0
perdidas= 0
while True:
    if contador == 1:
        confirmar_jugar = input("S si desea jugar y N si no quiere jugar:")
    else:
        confirmar_jugar = input("Si quieres volver a jugar presione S y si quiere dejar de jugar presione N: ")
        perdidas=contador-ganadas-1
    if confirmar_jugar.upper() == "S":
        print("Vamos a jugar, suerte.")
        primer_numero = random.randrange(10)
        segundo_numero = random.randrange(10)
        tercer_numero = random.randrange(10)
        cuarto_numero = random.randrange(10)
        if primer_numero != segundo_numero and primer_numero != tercer_numero and primer_numero != cuarto_numero and segundo_numero != tercer_numero and segundo_numero != cuarto_numero and tercer_numero != cuarto_numero:
            print(primer_numero, segundo_numero, tercer_numero, cuarto_numero)
        else:
            while primer_numero == segundo_numero or primer_numero == tercer_numero or primer_numero == cuarto_numero or segundo_numero == tercer_numero or segundo_numero == cuarto_numero or tercer_numero == cuarto_numero:
                primer_numero = random.randrange(10)
                segundo_numero = random.randrange(10)
                tercer_numero = random.randrange(10)
                cuarto_numero = random.randrange(10)
            print(primer_numero, segundo_numero, tercer_numero, cuarto_numero)
        famas = 0
        toques = 0
        turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
        for partidas in range(turnos_a_jugar):
            turno = partidas + 1
            intento = input(f"{turno}) ingrese los numeros: ")
            if len(intento) == 4:
                print("Tus resultados del turno son:")
                if(str(primer_numero)==intento[0]):
                    famas = famas + 1
                elif(str(primer_numero) == intento[1] or str(primer_numero) == intento[2] or str(primer_numero) == intento[3]):
                    toques = toques + 1
                if(str(segundo_numero)==intento[1]):
                    famas = famas + 1
                elif(str(segundo_numero) == intento[0] or str(segundo_numero) == intento[2] or str(segundo_numero) == intento[3]):
                    toques = toques + 1
                if(str(tercer_numero)==intento[2]):
                    famas = famas + 1
                elif(str(tercer_numero) == intento[0] or str(tercer_numero) == intento[1] or str(tercer_numero) == intento[3]):
                    toques = toques + 1
                if(str(cuarto_numero)==intento[3]):
                    famas = famas + 1
                elif(str(cuarto_numero) == intento[0] or str(cuarto_numero) == intento[1] or str(cuarto_numero) == intento[2]):
                    toques = toques + 1
                if(famas==0):
                    print("Famas=0")
                elif(famas == 1):
                    print("Famas=1")
                elif(famas == 2):
                    print("Famas=2")
                elif(famas == 3):
                    print("Famas=3")
                elif(famas == 4):
                    print("Famas=4 !!FELICIDADES GANASTE¡¡, has acertado en",turno,"intentos")
                    ganadas+=1
                    break
                if(toques==0):
                    print("Toques=0")
                elif(toques == 1):
                    print("Toques=1")
                elif(toques == 2):
                    print("Toques=2")
                elif(toques == 3):
                    print("Toques=3")
                elif(toques == 4):
                    print("Toques=4")
                famas = 0
                toques = 0
            else:
                print("El usuario pierde su jugada, por ingresar un dato invalido.")
                break
    elif confirmar_jugar.upper() == "N":
        print("Espero que quieras volver a jugar.")
        print("Partidas jugadas:", contador-1,"-", "Partidas Ganadas:",ganadas,"-", "Partidas perdidas:", perdidas)
        exit()
    else:
        print("Esta opción no está permitida")

    contador += 1
