#Trabajo de toque y queda
# Con Sofia Castro, Anibal Muñoz y Victor Camero
import random



#El for es para la cantidad de turnos a jugar

def numeros_azar():
     dig1 = random.randrange(10)
     dig2 = random.randrange(10)
     dig3 = random.randrange(10)
     dig4 = random.randrange(10)
     if dig1 != dig2 and dig1 != dig3 and dig1 != dig4 and dig2 != dig3 and dig2 != dig4 and dig3 != dig4:
         print(dig1, dig2, dig3, dig4)
     else:
          print("Vuelva a correr el programa")

print(numeros_azar())

turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
for partidas in range(turnos_a_jugar):
    turno = partidas + 1
    intento = input(f"{turno} ingrese los numeros:")




