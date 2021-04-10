#Trabajo de toque y queda
# Con Sofia Castro, Anibal Muñoz y Victor Camero
#hola

import random

dig1 = random.randrange(10)
dig2 = random.randrange(10)
dig3 = random.randrange(10)
dig4 = random.randrange(10)

if dig1 != dig2 and dig1 != dig3 and dig1 != dig4 and dig2 != dig3 and dig2 != dig4 and dig3 != dig4:
    print(dig1, dig2, dig3, dig4)
else:
    print("Vuelva a correr el programa")