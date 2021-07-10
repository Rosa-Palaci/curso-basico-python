#Aprendiendo a no repetir código con funciones
'''
def imprimir_mensaje():
    print('Mensaje especial: ')
    print('¡Estoy aprendiendo a usar funciones!')


imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()
'''
def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adiós')


opcion = int(input('Elige una opción(1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')    
else:
    print('Escribe la opción correcta')
'''
# 17 -Modularizando nuestro conversor de monedas
def suma (a, b):
    print('Se suma dos números')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)
'''