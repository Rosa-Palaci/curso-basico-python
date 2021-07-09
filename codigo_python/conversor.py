#Varios países en mi conversor de monedas
menu = """
Bienvenido al converso de monedas😎
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: 
"""
opcion = input(menu)

if opcion == '1':
    pass

pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $"+ dolares + " dólares" )

#Reto inverso
dolar = input("\n¿Cuántos dólares tienes?: ")
dolar = float(dolar)
valor_pesos_mexicano = 0.050
peso = dolar / valor_pesos_mexicano
peso = round(peso, 2)
peso = str(peso)
print("Tienes $"+ peso + "  pesos mexicanos" )