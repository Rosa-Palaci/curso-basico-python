#Proyecto: prueba de primalidad

#un número primo es el número que solo se puede
# dividir solo se entre si mismo y uno
#números primos entre 1-100: 2,3,5,7,11,13,17,
# 19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,
# 83,89,97
#Con lo anterior en mente el reto es 

def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue #saltear o no contar
        if numero % i == 0:
            contador += 1 #igual si escribo contador = contador + 1
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()