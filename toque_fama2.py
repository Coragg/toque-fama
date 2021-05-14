import random
print("------------------------------------------------------------------------------")
print("Bienvenido al juego: toque y fama")
print("El objetivo del juego es generar de manera aleatoria de 3 a 8 números\n"
      "del cero al nueve, tu deber es encontrarlos con las siguientes pistas\n"
      "si tienes 1 toque encontraste 1 número pero no en el lugar indicado\n"
      "si encontraste 1 fama encontraste 1 número y en el lugar indicado\n"
      "si logras todas las famas, felicidades ganaste")
print("Nota: si ingresa un número con mas digitos del que indico o números repetidos, usted pierde su partida")
print("------------------------------------------------------------------------------")
famas = 0
ganaste = 0
cantidad_partidas = 0
partidas_perdidas = 0
contador = 0
while True:
    if contador > 0:
        confirmar_jugar = int(input("¿Deseas jugar nuevamente? 1. Sí / 0. No:"))
    else:
        confirmar_jugar = int(input("¿Desea jugar? 1. Sí / 0. No: "))
    if confirmar_jugar == 1:
        cantidad_partidas += 1
        codigo = ''
        cantidad = int(input("Elige el largo del numero: "))
        while cantidad < 4 or cantidad > 9:
            cantidad = int(input("Elige el largo del numero: "))
        for digitos in range(cantidad):
            cifra = random.randint(0, 9)

            while str(cifra) in codigo:
                cifra = random.randint(0, 9)
            codigo = codigo + str(cifra)
        print(codigo)
        print("Bienvenido a Toque y Fama")
        print("Tienes que adivinar un numero de", 4, "cifras distintas")
        contador = 1
        intentos = 0
        intento = 0
        contar = 0
        while contador <= cantidad:
            intento += 1
            numeros = input(f"Intento {intento}: ")
            if numeros != codigo:
                intentos += 1
                famas = 0
                toque = 0
                contar += 1
                for recorrer_digitos in range(cantidad):
                    if numeros[recorrer_digitos] == codigo[recorrer_digitos]:
                        famas += 1
                    elif numeros[recorrer_digitos] in codigo:
                        toque += 1
                print("toques:", toque, "Famas: ", famas)

            elif numeros == codigo:
                intentos += 1
                ganaste += 1
                print("¡Felicitaciones! Has acertado en", intentos, "intentos")
                break

            if contar == cantidad:
                if famas < cantidad:
                    print("Fin del Juego La secuencia era", codigo)

            contador += 1
    elif confirmar_jugar == 0:
        partidas_perdidas = cantidad_partidas - ganaste
        print("Jugados:", cantidad_partidas, "Ganados:", ganaste, "Perdidos:", partidas_perdidas)
        exit()