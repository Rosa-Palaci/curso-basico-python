#Clase 27 
#Proyecto: videojuego

#Adivina el número: la computadora va a pensar 
# en un número aleatorio entre el 1 al 100, 
# si nosotro atinamos la computadora va a 
# decir que ganamos si no me va a decir que 
# el núm es mas grande o mas pequeño.
# adivina-el-numero.py


#Modulo: paquete de código disponible para poder
# ejecutar funciones

import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__': #interpoint
    run()