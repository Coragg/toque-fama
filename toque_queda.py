#Trabajo de toque y fama
# Con Sofia Castro, Anibal Muñoz y Victor Camero
import random
print("------------------------------------------------------------------------------")
print("Bienvenido al juego: toque y fama")
print("El objetivo del juego: el juego generara de manera aleatoria 4 numeros\n"
      "del cero al nueve, tu deber es encontrarlos con las siguientes pistas\n"
      "si tienes 1 toque encontraste 1 numero pero no en el lugar indicado\n"
      "si encontraste 1 fama encontraste 1 numero y en el lugar indicado\n"
      "si logras todas las famas, felicidades ganaste")
print("------------------------------------------------------------------------------")
contador = 1
ganadas = 0
famas = 0
perdidas = 0
cantidad_digitos = 0
primer_numero_aleatorio = 0
segundo_numero_aleatorio = 0
tercer_numero_aleatorio = 0
cuarto_numero_aleatorio = 0
quinto_numero_aleatorio = 0
sexto_numero_aleatorio = 0
septimo_numero_aleatorio = 0
octavo_numero_aleatorio = 0

while True:
    if contador == 1:
        confirmar_jugar = input("S si desea jugar y N si no quiere jugar:")
    else:
        if cantidad_digitos == 4:
            print("Fin del juego, la secuencia era", primer_numero_aleatorio, segundo_numero_aleatorio,
                  tercer_numero_aleatorio, cuarto_numero_aleatorio)
        elif cantidad_digitos == 5:
            print("Fin del juego, la secuencia era", primer_numero_aleatorio, segundo_numero_aleatorio,
                  tercer_numero_aleatorio, cuarto_numero_aleatorio, quinto_numero_aleatorio)
        elif cantidad_digitos == 6:
            print("Fin del juego, la secuencia era", primer_numero_aleatorio, segundo_numero_aleatorio,
                  tercer_numero_aleatorio, cuarto_numero_aleatorio, quinto_numero_aleatorio, sexto_numero_aleatorio)
        elif cantidad_digitos == 7:
            print("Fin del juego, la secuencia era", primer_numero_aleatorio, segundo_numero_aleatorio,
                  tercer_numero_aleatorio, cuarto_numero_aleatorio, quinto_numero_aleatorio, sexto_numero_aleatorio,
                  septimo_numero_aleatorio)
        elif cantidad_digitos == 8:
            print("Fin del juego, la secuencia era", primer_numero_aleatorio, segundo_numero_aleatorio,
                  tercer_numero_aleatorio, cuarto_numero_aleatorio, quinto_numero_aleatorio, sexto_numero_aleatorio,
                  septimo_numero_aleatorio, octavo_numero_aleatorio)
        confirmar_jugar = input("Si quieres volver a jugar presione S y si quiere dejar de jugar presione N: ")
        perdidas = contador - ganadas - 1
    if confirmar_jugar.upper() == "S":
        cantidad_digitos = int(input("Ingrese la cantidad de digitos a jugar(de 4 a 8):"))
        while cantidad_digitos < 4 or cantidad_digitos > 8:
            cantidad_digitos = int(input("Ingrese la cantidad de digitos a jugar(de 4 a 8):"))
        if cantidad_digitos == 4:
            print("Vamos a jugar, suerte.")
            print("------------------------------------------------------------------------------")
            primer_numero_aleatorio = random.randrange(10)
            segundo_numero_aleatorio = random.randrange(10)
            tercer_numero_aleatorio = random.randrange(10)
            cuarto_numero_aleatorio = random.randrange(10)

            while primer_numero_aleatorio == segundo_numero_aleatorio or primer_numero_aleatorio == tercer_numero_aleatorio or primer_numero_aleatorio == cuarto_numero_aleatorio or segundo_numero_aleatorio == tercer_numero_aleatorio or segundo_numero_aleatorio == cuarto_numero_aleatorio or tercer_numero_aleatorio == cuarto_numero_aleatorio:
                primer_numero_aleatorio = random.randrange(10)
                segundo_numero_aleatorio = random.randrange(10)
                tercer_numero_aleatorio = random.randrange(10)
                cuarto_numero_aleatorio = random.randrange(10)
            print(primer_numero_aleatorio, segundo_numero_aleatorio, tercer_numero_aleatorio, cuarto_numero_aleatorio)
            famas = 0
            toques = 0
            turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
            for partidas in range(turnos_a_jugar):
                turno = partidas + 1
                intento = input(f"{turno}) ingrese los numeros: ")
                if len(intento) == 4:
                    print("Tus resultados del turno son:")

                    if int(intento[0]) != int(intento[1]) and int(intento[0]) != int(intento[2]) and int(intento[0]) != int(intento[3]) and int(intento[1]) != int(intento[2]) and int(intento[1]) != int(intento[3]) and int(intento[2]) != int(intento[3]):
                        if(primer_numero_aleatorio == int(intento[0])):
                            famas = famas + 1
                        elif primer_numero_aleatorio == int(intento[1]) or primer_numero_aleatorio == int(intento[2]) or primer_numero_aleatorio == int(intento[3]):
                            toques = toques + 1
                        if(segundo_numero_aleatorio == int(intento[1])):
                            famas = famas + 1
                        elif(segundo_numero_aleatorio == int(intento[0]) or segundo_numero_aleatorio == int(intento[2]) or segundo_numero_aleatorio == int(intento[3])):
                            toques = toques + 1
                        if(tercer_numero_aleatorio == int(intento[2])):
                            famas = famas + 1
                        elif(tercer_numero_aleatorio == int(intento[0]) or tercer_numero_aleatorio == int(intento[1]) or tercer_numero_aleatorio == int(intento[3])):
                            toques = toques + 1
                        if(cuarto_numero_aleatorio == int(intento[3])):
                            famas = famas + 1
                        elif(cuarto_numero_aleatorio == int(intento[0]) or cuarto_numero_aleatorio == int(intento[1]) or cuarto_numero_aleatorio == int(intento[2])):
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
                            print("Famas=4 ¡¡FELICIDADES GANASTE!!, Has acertado en el intento", turno)
                            print("------------------------------------------------------------------------------")
                            ganadas += 1
                            break
                        if(toques == 0):
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
                    elif famas < 4:
                         print("Fin del juego, la secuencia era", primer_numero_aleatorio, segundo_numero_aleatorio,
                               tercer_numero_aleatorio, cuarto_numero_aleatorio)
                    else:
                        print("Se invalida este intento al tener números repetidos")
                        break
                else:
                    print("El usuario pierde su jugada, por ingresar un dato invalido.")
                    break

        elif cantidad_digitos == 5:
            print("Vamos a jugar, suerte.")
            print("------------------------------------------------------------------------------")
            primer_numero_aleatorio = random.randrange(10)
            segundo_numero_aleatorio = random.randrange(10)
            tercer_numero_aleatorio = random.randrange(10)
            cuarto_numero_aleatorio = random.randrange(10)
            quinto_numero_aleatorio = random.randrange(10)
            while primer_numero_aleatorio == segundo_numero_aleatorio or primer_numero_aleatorio == tercer_numero_aleatorio or primer_numero_aleatorio == cuarto_numero_aleatorio or primer_numero_aleatorio == quinto_numero_aleatorio or segundo_numero_aleatorio == tercer_numero_aleatorio or segundo_numero_aleatorio == cuarto_numero_aleatorio or segundo_numero_aleatorio == quinto_numero_aleatorio or tercer_numero_aleatorio == cuarto_numero_aleatorio or tercer_numero_aleatorio == quinto_numero_aleatorio or cuarto_numero_aleatorio == quinto_numero_aleatorio:
                primer_numero_aleatorio = random.randrange(10)
                segundo_numero_aleatorio = random.randrange(10)
                tercer_numero_aleatorio = random.randrange(10)
                cuarto_numero_aleatorio = random.randrange(10)
                quinto_numero_aleatorio = random.randrange(10)
            print(primer_numero_aleatorio,segundo_numero_aleatorio,tercer_numero_aleatorio,cuarto_numero_aleatorio,quinto_numero_aleatorio)
            famas = 0
            toques = 0
            turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
            for partidas in range(turnos_a_jugar):
                turno = partidas + 1
                intento = input(f"{turno}) ingrese los numeros: ")
                if len(intento) == 5:
                    print("Tus resultados del turno son:")

                    if int(intento[0]) != int(intento[1]) and int(intento[0]) != int(intento[2]) \
                            and int(intento[0]) != int(intento[3]) and int(intento[0]) != int(intento[4]) \
                            and int(intento[1]) != int(intento[2]) and int(intento[1]) != int(intento[3]) \
                            and int(intento[1]) != int(intento[4]) and int(intento[2]) != int(intento[3])\
                            and int(intento[2]) != int(intento[4]) and int(intento[3] != int(intento[4])):
                        if(primer_numero_aleatorio == int(intento[0])):
                            famas = famas + 1
                        elif primer_numero_aleatorio == int(intento[1]) or primer_numero_aleatorio == int(intento[2]) or primer_numero_aleatorio == int(intento[3]) or primer_numero_aleatorio == int(intento[4]):
                            toques = toques + 1
                        if(segundo_numero_aleatorio == int(intento[1])):
                            famas = famas + 1
                        elif(segundo_numero_aleatorio == int(intento[0]) or segundo_numero_aleatorio == int(intento[2]) or segundo_numero_aleatorio == int(intento[3]) or segundo_numero_aleatorio == int(intento[4])):
                            toques = toques + 1
                        if(tercer_numero_aleatorio == int(intento[2])):
                            famas = famas + 1
                        elif(tercer_numero_aleatorio == int(intento[0]) or tercer_numero_aleatorio == int(intento[1]) or tercer_numero_aleatorio == int(intento[3]) or tercer_numero_aleatorio == int(intento[4])):
                            toques = toques + 1
                        if(cuarto_numero_aleatorio == int(intento[3])):
                            famas = famas + 1
                        elif(cuarto_numero_aleatorio == int(intento[0]) or cuarto_numero_aleatorio == int(intento[1]) or cuarto_numero_aleatorio == int(intento[2]) or cuarto_numero_aleatorio == int(intento[4])):
                            toques = toques + 1
                        if(quinto_numero_aleatorio == int(intento[4])):
                            famas = famas + 1
                        elif(quinto_numero_aleatorio == int(intento[0]) or quinto_numero_aleatorio == int(intento[1]) or quinto_numero_aleatorio == int(intento[2]) or quinto_numero_aleatorio == int(intento[3])):
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
                            print("Famas=4")
                        elif(famas == 5):
                            print("Famas=5  ¡¡FELICIDADES GANASTE!!, Has acertado en el intento", turno)
                            print("------------------------------------------------------------------------------")
                            ganadas += 1
                            break
                        if(toques == 0):
                            print("Toques=0")
                        elif(toques == 1):
                            print("Toques=1")
                        elif(toques == 2):
                            print("Toques=2")
                        elif(toques == 3):
                            print("Toques=3")
                        elif(toques == 4):
                            print("Toques=4")
                        elif(toques == 5):
                            print("toques=5")
                        famas = 0
                        toques = 0
                    else:
                        print("Se invalida este intento al tener números repetidos")
                        break
                else:
                    print("El usuario pierde su jugada, por ingresar un dato invalido.")
                    break

        elif cantidad_digitos == 6:
            print("Vamos a jugar, suerte.")
            print("------------------------------------------------------------------------------")
            primer_numero_aleatorio = random.randrange(10)
            segundo_numero_aleatorio = random.randrange(10)
            tercer_numero_aleatorio = random.randrange(10)
            cuarto_numero_aleatorio = random.randrange(10)
            quinto_numero_aleatorio = random.randrange(10)
            sexto_numero_aleatorio = random.randrange(10)
            while primer_numero_aleatorio == segundo_numero_aleatorio or primer_numero_aleatorio == tercer_numero_aleatorio \
                    or primer_numero_aleatorio == cuarto_numero_aleatorio or primer_numero_aleatorio == quinto_numero_aleatorio \
                    or primer_numero_aleatorio == sexto_numero_aleatorio or segundo_numero_aleatorio == tercer_numero_aleatorio \
                    or segundo_numero_aleatorio == cuarto_numero_aleatorio or segundo_numero_aleatorio == quinto_numero_aleatorio \
                    or segundo_numero_aleatorio == sexto_numero_aleatorio or tercer_numero_aleatorio == cuarto_numero_aleatorio \
                    or tercer_numero_aleatorio == quinto_numero_aleatorio or tercer_numero_aleatorio == sexto_numero_aleatorio \
                    or cuarto_numero_aleatorio == quinto_numero_aleatorio or cuarto_numero_aleatorio == sexto_numero_aleatorio \
                    or quinto_numero_aleatorio == sexto_numero_aleatorio:
                primer_numero_aleatorio = random.randrange(10)
                segundo_numero_aleatorio = random.randrange(10)
                tercer_numero_aleatorio = random.randrange(10)
                cuarto_numero_aleatorio = random.randrange(10)
                quinto_numero_aleatorio = random.randrange(10)
                sexto_numero_aleatorio = random.randrange(10)
            print(primer_numero_aleatorio,segundo_numero_aleatorio,tercer_numero_aleatorio,cuarto_numero_aleatorio,quinto_numero_aleatorio,sexto_numero_aleatorio)
            famas = 0
            toques = 0
            turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
            for partidas in range(turnos_a_jugar):
                turno = partidas + 1
                intento = input(f"{turno}) ingrese los numeros: ")
                if len(intento) == 6:
                    print("Tus resultados del turno son:")

                    if int(intento[0]) != int(intento[1]) and int(intento[0]) != int(intento[2]) and int(
                            intento[0]) != int(intento[3]) and intento[0]!= int(intento[4]) and int(intento[0]) != int(intento[5]) and int(intento[1]) != int(intento[2]) and int(
                            intento[1]) != int(intento[3]) and int(intento[2]) != int(intento[3] and int(intento[1]) != int(intento) != int(intento[4]) and int(intento[1]) != int(intento[5])):
                        if (primer_numero_aleatorio == int(intento[0])):
                            famas = famas + 1
                        elif primer_numero_aleatorio == int(intento[1]) or primer_numero_aleatorio == int(
                                intento[2]) or primer_numero_aleatorio == int(
                                intento[3]) or primer_numero_aleatorio == int(intento[4]) or primer_numero_aleatorio == int(intento[5]):
                            toques = toques + 1
                        if (segundo_numero_aleatorio == int(intento[1])):
                            famas = famas + 1
                        elif (segundo_numero_aleatorio == int(intento[0]) or segundo_numero_aleatorio == int(
                                intento[2]) or segundo_numero_aleatorio == int(
                                intento[3]) or segundo_numero_aleatorio == int(intento[4]) or segundo_numero_aleatorio == int(intento[5])):
                            toques = toques + 1
                        if (tercer_numero_aleatorio == int(intento[2])):
                            famas = famas + 1
                        elif (tercer_numero_aleatorio == int(intento[0]) or tercer_numero_aleatorio == int(
                                intento[1]) or tercer_numero_aleatorio == int(
                                intento[3]) or tercer_numero_aleatorio == int(intento[4]) or tercer_numero_aleatorio == int(intento[5])):
                            toques = toques + 1
                        if (cuarto_numero_aleatorio == int(intento[3])):
                            famas = famas + 1
                        elif (cuarto_numero_aleatorio == int(intento[0]) or cuarto_numero_aleatorio == int(
                                intento[1]) or cuarto_numero_aleatorio == int(
                                intento[2]) or cuarto_numero_aleatorio == int(intento[4]) or cuarto_numero_aleatorio == int(intento[5])):
                            toques = toques + 1
                        if (quinto_numero_aleatorio == int(intento[4])):
                            famas = famas + 1
                        elif (quinto_numero_aleatorio == int(intento[0]) or quinto_numero_aleatorio == int(
                                intento[1]) or quinto_numero_aleatorio == int(
                                intento[2]) or quinto_numero_aleatorio == int(intento[3]) or quinto_numero_aleatorio == int(intento[5])):
                            toques = toques + 1
                        if (sexto_numero_aleatorio == int(intento[5])):
                            famas = famas + 1
                        elif (sexto_numero_aleatorio == int(intento[0]) or sexto_numero_aleatorio == int(intento[1]) or sexto_numero_aleatorio == int(intento[2]) or sexto_numero_aleatorio == int(intento[3]) or sexto_numero_aleatorio == int(intento[4])):
                            toques = toques + 1
                        if (famas == 0):
                            print("Famas=0")
                        elif (famas == 1):
                            print("Famas=1")
                        elif (famas == 2):
                            print("Famas=2")
                        elif (famas == 3):
                            print("Famas=3")
                        elif (famas == 4):
                            print("Famas=4")
                        elif (famas == 5):
                            print("Famas=5")
                        elif (famas == 6):
                            print("Famas=6 ¡¡FELICIDADES GANASTE!!, Has acertado en el intento", turno)
                            print("------------------------------------------------------------------------------")
                            ganadas += 1
                            break
                        if (toques == 0):
                            print("Toques=0")
                        elif (toques == 1):
                            print("Toques=1")
                        elif (toques == 2):
                            print("Toques=2")
                        elif (toques == 3):
                            print("Toques=3")
                        elif (toques == 4):
                            print("Toques=4")
                        elif (toques == 5):
                            print("Toques=5")
                        elif (toques == 6):
                            print("Toques=6")
                        famas = 0
                        toques = 0
                    else:
                        print("Se invalida este intento al tener números repetidos")
                        break
                else:
                    print("El usuario pierde su jugada, por ingresar un dato invalido.")
                    break

        elif cantidad_digitos == 7:
            print("Vamos a jugar, suerte.")
            print("------------------------------------------------------------------------------")
            primer_numero_aleatorio = random.randrange(10)
            segundo_numero_aleatorio = random.randrange(10)
            tercer_numero_aleatorio = random.randrange(10)
            cuarto_numero_aleatorio = random.randrange(10)
            quinto_numero_aleatorio = random.randrange(10)
            sexto_numero_aleatorio = random.randrange(10)
            while primer_numero_aleatorio == segundo_numero_aleatorio or primer_numero_aleatorio == tercer_numero_aleatorio \
                    or primer_numero_aleatorio == cuarto_numero_aleatorio or primer_numero_aleatorio == quinto_numero_aleatorio \
                    or primer_numero_aleatorio == sexto_numero_aleatorio or primer_numero_aleatorio == septimo_numero_aleatorio or segundo_numero_aleatorio == tercer_numero_aleatorio \
                    or segundo_numero_aleatorio == cuarto_numero_aleatorio or segundo_numero_aleatorio == quinto_numero_aleatorio \
                    or segundo_numero_aleatorio == sexto_numero_aleatorio or segundo_numero_aleatorio == septimo_numero_aleatorio or tercer_numero_aleatorio == cuarto_numero_aleatorio \
                    or tercer_numero_aleatorio == quinto_numero_aleatorio or tercer_numero_aleatorio == sexto_numero_aleatorio \
                    or tercer_numero_aleatorio == sexto_numero_aleatorio or tercer_numero_aleatorio == septimo_numero_aleatorio\
                    or cuarto_numero_aleatorio == quinto_numero_aleatorio or cuarto_numero_aleatorio == sexto_numero_aleatorio  or cuarto_numero_aleatorio == quinto_numero_aleatorio\
                    or quinto_numero_aleatorio == sexto_numero_aleatorio or quinto_numero_aleatorio == septimo_numero_aleatorio or sexto_numero_aleatorio == septimo_numero_aleatorio:
                primer_numero_aleatorio = random.randrange(10)
                segundo_numero_aleatorio = random.randrange(10)
                tercer_numero_aleatorio = random.randrange(10)
                cuarto_numero_aleatorio = random.randrange(10)
                quinto_numero_aleatorio = random.randrange(10)
                sexto_numero_aleatorio = random.randrange(10)
                septimo_numero_aleatorio = random.randrange(10)
            print(primer_numero_aleatorio, segundo_numero_aleatorio, tercer_numero_aleatorio, cuarto_numero_aleatorio, quinto_numero_aleatorio, sexto_numero_aleatorio, septimo_numero_aleatorio)
            famas = 0
            toques = 0
            turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
            for partidas in range(turnos_a_jugar):
                turno = partidas + 1
                intento = input(f"{turno}) ingrese los numeros: ")
                if len(intento) == 7:
                    print("Tus resultados del turno son:")

                    if int(intento[0]) != int(intento[1]) and int(intento[0]) != int(intento[2]) and \
                            int(intento[0]) != int(intento[3]) and int(intento[0]) != int(intento[4]) and \
                            int(intento[0]) != int(intento[5]) and int(intento[0]) != int(intento[6]) and \
                            int(intento[0]) != int(intento[7]) and int(intento[1]) != int(intento[2]) and \
                            int(intento[1]) != int(intento[3]):
                        if (primer_numero_aleatorio == int(intento[0])):
                            famas = famas + 1
                        elif primer_numero_aleatorio == int(intento[1]) or primer_numero_aleatorio == int(
                                intento[2]) or primer_numero_aleatorio == int(
                                intento[3]) or primer_numero_aleatorio == int(intento[4]) or primer_numero_aleatorio == int(intento[5]) or primer_numero_aleatorio == int(intento[6]):
                            toques = toques + 1
                        if (segundo_numero_aleatorio == int(intento[1])):
                            famas = famas + 1
                        elif (segundo_numero_aleatorio == int(intento[0]) or segundo_numero_aleatorio == int(
                                intento[2]) or segundo_numero_aleatorio == int(
                                intento[3]) or segundo_numero_aleatorio == int(intento[4]) or segundo_numero_aleatorio == int(intento[5]) or segundo_numero_aleatorio == int(intento[6])):
                            toques = toques + 1
                        if (tercer_numero_aleatorio == int(intento[2])):
                            famas = famas + 1
                        elif (tercer_numero_aleatorio == int(intento[0]) or tercer_numero_aleatorio == int(
                                intento[1]) or tercer_numero_aleatorio == int(
                                intento[3]) or tercer_numero_aleatorio == int(intento[4]) or tercer_numero_aleatorio == int(intento[5]) or tercer_numero_aleatorio == int(intento[6])):
                            toques = toques + 1
                        if (cuarto_numero_aleatorio == int(intento[3])):
                            famas = famas + 1
                        elif (cuarto_numero_aleatorio == int(intento[0]) or cuarto_numero_aleatorio == int(
                                intento[1]) or cuarto_numero_aleatorio == int(
                                intento[2]) or cuarto_numero_aleatorio == int(intento[4]) or cuarto_numero_aleatorio == int(intento[5]) or cuarto_numero_aleatorio == int(intento[6])):
                            toques = toques + 1
                        if (quinto_numero_aleatorio == int(intento[4])):
                            famas = famas + 1
                        elif (quinto_numero_aleatorio == int(intento[0]) or quinto_numero_aleatorio == int(
                                intento[1]) or quinto_numero_aleatorio == int(
                                intento[2]) or quinto_numero_aleatorio == int(intento[3]) or quinto_numero_aleatorio == int(intento[5]) or quinto_numero_aleatorio == int(intento[6])):
                            toques = toques + 1
                        if (sexto_numero_aleatorio == int(intento[5])):
                            famas = famas + 1
                        elif (sexto_numero_aleatorio == int(intento[0]) or sexto_numero_aleatorio == int(intento[1]) or sexto_numero_aleatorio == int(intento[2]) or sexto_numero_aleatorio == int(intento[3]) or sexto_numero_aleatorio == int(intento[4]) or sexto_numero_aleatorio == int(intento[6])):
                            toques = toques + 1
                        if (septimo_numero_aleatorio == int(intento[6])):
                            famas = famas + 1
                        elif (septimo_numero_aleatorio == int(intento[0]) or septimo_numero_aleatorio == int(intento[1]) or septimo_numero_aleatorio == int(intento[2]) or septimo_numero_aleatorio == int(intento[3]) or septimo_numero_aleatorio == int(intento[4]) or septimo_numero_aleatorio == int(intento[5])):
                            toques = toques + 1
                        if (famas == 0):
                            print("Famas=0")
                        elif (famas == 1):
                            print("Famas=1")
                        elif (famas == 2):
                            print("Famas=2")
                        elif (famas == 3):
                            print("Famas=3")
                        elif (famas == 4):
                            print("Famas=4")
                        elif (famas == 5):
                            print("Famas=5")
                        elif (famas == 6):
                            print("Famas=6")
                        elif (famas == 7):
                            print("Famas=7 ¡¡FELICIDADES GANASTE!!, Has acertado en el intento", turno)
                            print("------------------------------------------------------------------------------")
                            ganadas += 1
                            break
                        if (toques == 0):
                            print("Toques=0")
                        elif (toques == 1):
                            print("Toques=1")
                        elif (toques == 2):
                            print("Toques=2")
                        elif (toques == 3):
                            print("Toques=3")
                        elif (toques == 4):
                            print("Toques=4")
                        elif (toques == 5):
                            print("Toques=5")
                        elif (toques == 6):
                            print("Toques=6")
                        elif (toques == 7):
                            print("Toques=7")
                        famas = 0
                        toques = 0
                    else:
                        print("Se invalida este intento al tener números repetidos")
                        break
                else:
                    print("El usuario pierde su jugada, por ingresar un dato invalido. ")
                    break

        elif cantidad_digitos == 8:
            primer_numero_aleatorio = random.randrange(10)
            segundo_numero_aleatorio = random.randrange(10)
            tercer_numero_aleatorio = random.randrange(10)
            cuarto_numero_aleatorio = random.randrange(10)
            quinto_numero_aleatorio = random.randrange(10)
            sexto_numero_aleatorio = random.randrange(10)
            septimo_numero_aleatorio = random.randrange(10)
            octavo_numero_aleatorio = random.randrange(10)
            while primer_numero_aleatorio == segundo_numero_aleatorio or primer_numero_aleatorio == tercer_numero_aleatorio \
                    or primer_numero_aleatorio == cuarto_numero_aleatorio or primer_numero_aleatorio == quinto_numero_aleatorio \
                    or primer_numero_aleatorio == sexto_numero_aleatorio or segundo_numero_aleatorio == tercer_numero_aleatorio \
                    or segundo_numero_aleatorio == cuarto_numero_aleatorio or segundo_numero_aleatorio == quinto_numero_aleatorio \
                    or segundo_numero_aleatorio == sexto_numero_aleatorio or tercer_numero_aleatorio == cuarto_numero_aleatorio \
                    or tercer_numero_aleatorio == quinto_numero_aleatorio or tercer_numero_aleatorio == sexto_numero_aleatorio \
                    or cuarto_numero_aleatorio == quinto_numero_aleatorio or cuarto_numero_aleatorio == sexto_numero_aleatorio \
                    or quinto_numero_aleatorio == sexto_numero_aleatorio or quinto_numero_aleatorio == septimo_numero_aleatorio \
                    or quinto_numero_aleatorio == octavo_numero_aleatorio or sexto_numero_aleatorio == septimo_numero_aleatorio \
                    or sexto_numero_aleatorio == octavo_numero_aleatorio or septimo_numero_aleatorio == octavo_numero_aleatorio :
                primer_numero_aleatorio = random.randrange(10)
                segundo_numero_aleatorio = random.randrange(10)
                tercer_numero_aleatorio = random.randrange(10)
                cuarto_numero_aleatorio = random.randrange(10)
                quinto_numero_aleatorio = random.randrange(10)
                sexto_numero_aleatorio = random.randrange(10)
                septimo_numero_aleatorio = random.randrange(10)
                octavo_numero_aleatorio = random.randrange(10)
            print(primer_numero_aleatorio, segundo_numero_aleatorio, tercer_numero_aleatorio,cuarto_numero_aleatorio, quinto_numero_aleatorio, sexto_numero_aleatorio,septimo_numero_aleatorio,octavo_numero_aleatorio)
            famas = 0
            toques = 0
            turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
            for partidas in range(turnos_a_jugar):
                turno = partidas + 1
                intento = input(f"{turno}) ingrese los numeros: ")
                if len(intento) == 8:
                    print("Tus resultados del turno son:")

                    if int(intento[0]) != int(intento[1]) and int(intento[0]) != int(intento[2]) \
                            and int(intento[0]) != int(intento[3]) and int(intento[0]) != int(intento[4]) \
                            and int(intento[0]) != int(intento[5]) and int(intento[0]) != int(intento[6]) \
                            and int(intento[0]) != int(intento[7]) and int(intento[1]) != int(intento[2]) \
                            and int(intento[1]) != int(intento[3]) and int(intento[2]) != int(intento[3]) \
                            and int(intento[1] != int(intento[4]) and int(intento[1]) != int(intento[5]) and int(intento[1]) != int(intento[6]) and int(intento[1]) != int(intento[7])):

                        if (primer_numero_aleatorio == int(intento[0])):
                            famas = famas + 1
                        elif primer_numero_aleatorio == int(intento[1]) or primer_numero_aleatorio == int(
                                intento[2]) or primer_numero_aleatorio == int(
                                intento[3]) or primer_numero_aleatorio == int(intento[4]) or primer_numero_aleatorio == int(intento[5]) or primer_numero_aleatorio == int(intento[6]) or primer_numero_aleatorio == int(intento[7]):
                            toques = toques + 1
                        if (segundo_numero_aleatorio == int(intento[1])):
                            famas = famas + 1
                        elif (segundo_numero_aleatorio == int(intento[0]) or segundo_numero_aleatorio == int(
                                intento[2]) or segundo_numero_aleatorio == int(
                                intento[3]) or segundo_numero_aleatorio == int(intento[4]) or segundo_numero_aleatorio == int(intento[5]) or segundo_numero_aleatorio == int(intento[6]) or segundo_numero_aleatorio == int(intento[7])):
                            toques = toques + 1
                        if (tercer_numero_aleatorio == int(intento[2])):
                            famas = famas + 1
                        elif (tercer_numero_aleatorio == int(intento[0]) or tercer_numero_aleatorio == int(
                                intento[1]) or tercer_numero_aleatorio == int(
                                intento[3]) or tercer_numero_aleatorio == int(intento[4]) or tercer_numero_aleatorio == int(intento[5]) or tercer_numero_aleatorio == int(intento[6]) or tercer_numero_aleatorio == int(intento[7])):
                            toques = toques + 1
                        if (cuarto_numero_aleatorio == int(intento[3])):
                            famas = famas + 1
                        elif (cuarto_numero_aleatorio == int(intento[0]) or cuarto_numero_aleatorio == int(
                                intento[1]) or cuarto_numero_aleatorio == int(
                                intento[2]) or cuarto_numero_aleatorio == int(intento[4]) or cuarto_numero_aleatorio == int(intento[5]) or cuarto_numero_aleatorio == int(intento[6]) or cuarto_numero_aleatorio == int(intento[7])):
                            toques = toques + 1
                        if (quinto_numero_aleatorio == int(intento[4])):
                            famas = famas + 1
                        elif (quinto_numero_aleatorio == int(intento[0]) or quinto_numero_aleatorio == int(
                                intento[1]) or quinto_numero_aleatorio == int(
                                intento[2]) or quinto_numero_aleatorio == int(intento[3]) or quinto_numero_aleatorio == int(intento[5]) or quinto_numero_aleatorio == int(intento[6]) or quinto_numero_aleatorio == int(intento[7])):
                            toques = toques + 1
                        if (sexto_numero_aleatorio == int(intento[5])):
                            famas = famas + 1
                        elif (sexto_numero_aleatorio == int(intento[0]) or sexto_numero_aleatorio == int(intento[1]) or sexto_numero_aleatorio == int(intento[2]) or sexto_numero_aleatorio == int(intento[3]) or sexto_numero_aleatorio == int(intento[4]) or sexto_numero_aleatorio == int(intento[6]) or sexto_numero_aleatorio == int(intento[7])):
                            toques = toques + 1
                        if (septimo_numero_aleatorio == int(intento[6])):
                            famas = famas + 1
                        elif (septimo_numero_aleatorio == int(intento[0]) or septimo_numero_aleatorio == int(intento[1]) or septimo_numero_aleatorio == int(intento[2]) or septimo_numero_aleatorio == int(intento[3]) or septimo_numero_aleatorio == int(intento[4]) or septimo_numero_aleatorio == int(intento[5]) or septimo_numero_aleatorio == int(intento[7])):
                            toques = toques + 1
                        if (octavo_numero_aleatorio == int(intento[7])):
                            famas = famas + 1
                        elif octavo_numero_aleatorio == int(intento[0]) or octavo_numero_aleatorio == int(intento[1]) or octavo_numero_aleatorio == int(intento[2]) or octavo_numero_aleatorio == int(intento[3]) or octavo_numero_aleatorio == int(intento[4]) or octavo_numero_aleatorio == int(intento[5]) or octavo_numero_aleatorio == int(intento[6]):
                            toques = toques + 1
                        if (famas == 0):
                            print("Famas=0")
                        elif (famas == 1):
                            print("Famas=1")
                        elif (famas == 2):
                            print("Famas=2")
                        elif (famas == 3):
                            print("Famas=3")
                        elif (famas == 4):
                            print("Famas=4")
                        elif (famas == 5):
                            print("Famas=5")
                        elif (famas == 6):
                            print("Famas=6")
                        elif (famas == 7):
                            print("Famas=7")
                        elif (famas == 8):
                            print("Famas=8 ¡¡FELICIDADES GANASTE!!, Has acertado en el intento", turno)
                            print("------------------------------------------------------------------------------")
                            ganadas += 1
                            break
                        if (toques == 0):
                            print("Toques=0")
                        elif (toques == 1):
                            print("Toques=1")
                        elif (toques == 2):
                            print("Toques=2")
                        elif (toques == 3):
                            print("Toques=3")
                        elif (toques == 4):
                            print("Toques=4")
                        elif (toques == 5):
                            print("Toques=5")
                        elif (toques == 6):
                            print("Toques=6")
                        elif (toques == 7):
                            print("Toques=7")
                        elif (toques == 8):
                            print("Toques=8")
                        famas = 0
                        toques = 0
                    else:
                        print("Se invalida este intento al tener números repetidos")
                        break
                else:
                    print("El usuario pierde su jugada, por ingresar un dato invalido.")
                    break

    elif confirmar_jugar.upper() == "N":
        print("------------------------------------------------------------------------------")
        print("Espero que quieras volver a jugar.")
        print("Partidas Jugadas:", contador - 1, "-", "Partidas Ganadas:", ganadas, "-", "Partidas Perdidas:", perdidas, "-", "Record de Intentos:")
        print("------------------------------------------------------------------------------")
        exit()
    else:
        print("Esta opción no está permitida")

    contador += 1