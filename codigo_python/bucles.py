'''
#Imprimir todas la potencial de 2 hasta llegar al numero 1000

for num_potencia in range(1, 1001):
    po = num_potencia**2
    print(po)

# print(num_potencia)

contador = 1
print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))
'''
def run():
    LIMITE = 1000 

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE: 
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()