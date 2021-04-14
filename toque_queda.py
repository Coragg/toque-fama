#Trabajo de toque y queda
# Con Sofia Castro, Anibal Muñoz y Victor Camero
import random

# Funcion de los numeros azar
def numeros_azar():
     primer_numero = random.randrange(10)
     segundo_numero = random.randrange(10)
     tercer_numero = random.randrange(10)
     cuarto_numero = random.randrange(10)
     if primer_numero != segundo_numero and primer_numero != tercer_numero and primer_numero != cuarto_numero and segundo_numero != tercer_numero and segundo_numero != cuarto_numero and tercer_numero != cuarto_numero:
         print(primer_numero, segundo_numero, tercer_numero, cuarto_numero)
     else:
          print("Vuelva a correr el programa")

print(numeros_azar())

turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
for partidas in range(turnos_a_jugar):
    turno = partidas + 1
    intento = input(f"{turno} ingrese los numeros:")




