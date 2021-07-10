#Varios países en mi conversor de monedas
#from codigo_python.funciones import conversacion

def conversor (tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " dólares" )

menu = """
Bienvenido al converso de monedas😎
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: 
"""
opcion = input(menu)

if opcion == '1':
    conversor("colombianos", 3875)
elif opcion == '2':
    conversor("argentinos", 65)
elif opcion == '3':
    conversor("mexicanos", 20)
else:
    print('Ingresa una opción correcta por favor')

# 17 - Modularizando nuestro conversor de monedas
#funcion que mejore el código