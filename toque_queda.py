#Trabajo de toque y queda
# Con Sofia Castro, Anibal Muñoz y Victor Camero
import random

# cuatro numeros aleatorios que no se repiten entre si
def numeros_azar():
    primer = random.randrange(10)
    segundo_numero = random.randrange(10)
    tercer_numero = random.randrange(10)
    cuarto_numero = random.randrange(10)
    while primer == segundo_numero or primer == tercer_numero or primer == cuarto_numero or segundo_numero == tercer_numero or segundo_numero == cuarto_numero or tercer_numero == cuarto_numero:
        primer = random.randrange(10)
        segundo_numero = random.randrange(10)
        tercer_numero = random.randrange(10)
        cuarto_numero = random.randrange(10)
    return primer, segundo_numero, tercer_numero, cuarto_numero



turnos_a_jugar = int(input("Ingrese los turnos a jugar:"))
for partidas in range(turnos_a_jugar):
    turno = partidas + 1
    intento = input(f"{turno} ingrese los numeros:")





