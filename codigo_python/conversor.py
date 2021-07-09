#Reto: conversor de monedas
pesos = input("¿Cuántos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 20
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