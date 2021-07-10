def run():
    '''
    for contador in range(1000):
        if contador % 2 != 0:#impirmir solo numeros pares-->
            continue
        print(contador)
    
    for i in range(10000):
        print(i)
        if i == 5678:
            break
    
    text = input('Escribe un texto: ')
    for letra in text:
        if letra == 'o':
            break
        print(letra)'''
#Reto donde utilice break y continue, ciclo while
def run():
    print('Este es mi reto utilizando ciclo while y break y continue')
    print('Completa el dicho')

    dichos = """
    Bienvenido al Cafe del Dicho 🤷‍♀️😉
    1 - Agua que no has de beber, ... 
    2 - Botellita de jerez, ... 
    3 - El flojo y el mezquino, ... 
    4 - No quiero jugar solo deme mi café 🤔

    Elige una mitad del dicho que quieras acompletar: 
    """ 
    dicho_elegido = input(dichos)
    respuesta_dada = input('Ingresa la otra parte del dicho: ')

    RESPUESTA = """
    1 = 'déjala correr'
    2 = 'todo lo que me digas será al revés'
    3 = 'recorren dos veces el mismo camino'
    """
    while respuesta_dada != (RESPUESTA + '{dicho_elegido}'): 
        print('Auch!' + str(respuesta_dada) + ' no es la otra mitad.')
        break
        


if __name__ == '__main__':
    run()