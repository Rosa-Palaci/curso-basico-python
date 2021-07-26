#Clase 30

def run():
    '''Un diccionario es una estructura de datos
    de llaves y valores, las llaves no son numeros
    que van del 1 al infinito. Las llaves definen
    los diccionarios nombre indice es la llave y los valores'''
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }
    # print(poblacion_paises['Brasil'])

    # for pais in poblacion_paises.keys(): 
    #     '''keys - llaves'''
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     '''values - valores'''
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        '''itesm - valores y llaves'''
        print(pais  + 'tiene '+ str(poblacion)+ ' habitantes')

if __name__ =='__main__':
    run()