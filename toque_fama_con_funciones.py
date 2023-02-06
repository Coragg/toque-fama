import random
import os

def rules_and_presentetion():
    """Introducion y reglas del juego""" 
    print("------------------------------------------------------------------------------------------------------------------")
    print("Bienvenido al juego: toque y fama")
    print("El objetivo del juego es generar de manera aleatoria de 3 a 8 números\n"
      "del cero al nueve, tu deber es encontrarlos con las siguientes pistas\n"
      "si tienes 1 toque encontraste 1 número pero no en el lugar indicado\n"
      "si encontraste 1 fama encontraste 1 número y en el lugar indicado\n"
      "si logras todas las famas, felicidades ganaste")
    print("Nota: si ingresa un número con mas digitos del que indico o números repetidos, usted pierde su partida")
    print("------------------------------------------------------------------------------------------------------------------")


def generate_randit_number(quantity_of_numbers: int):
    """ Crea un numero aleatorio en base a la cantidad de digitos definidos\n
    param int quantity_of_numbers \n
    return un str con numeros no repetidos entre si"""
    number = ''
    for digits in range(quantity_of_numbers):
        whole_number = random.randint(0, 9)
        while str(whole_number) in number:
            whole_number = random.randint(0, 9)
        number = number + str(whole_number)
    return number


def cantidad_toque_and_fama(random_number: str, user_number: str, cantidad: int):
    """ Dice cuantos toques y famas se han tenido con el intento \n
    param  \n
    param  \n
    param   \n
    return una lista con (fama: int, toque: int)"""
    fama, toque =  0 , 0
    for verification in range(cantidad):
        if user_number[verification] is random_number[verification]:
            fama += 1
        elif user_number[verification] in random_number:
            toque += 1
    return fama, toque


def game():
    digitos = int(input(''))
    turnos = int(input(""))


def close_game():
    """Cierre del programa y limpieza de la consola. """
    os.system('pause')
    os.system("cls")
    exit()


def invalid_argument():
    """indica la invalides del input de inicio o cierre"""
    print("Esta opcion es invalida.")
    print("Por lo cual, prueba otra vez con una opcion valida")


def consult_user():
    yes_or_no = input("Escribe si, si deseas jugar o no, si deseas cerrar el juego: ")
    if yes_or_no.lower() == "si":
        pass
    elif yes_or_no.lower() == "no":
        close_game()
    else:
        invalid_argument()


def main():
    rules_and_presentetion()
    consult_user()

if __name__ == '__main__':
    main()
