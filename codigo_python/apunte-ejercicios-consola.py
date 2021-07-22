Entendiendo cómo funcionan las tuplas

numeros = [1, 2, 3, 4, 5]
numeros
[1, 2, 3, 4, 5]
numeros.append('Hola')
numeros
[1, 2, 3, 4, 5, 'Hola']
numeros.pop(5)
'Hola'
numeros
[1, 2, 3, 4, 5]
'Hola' + ' ' + 'Mundo'
'Hola Mundo'
numeros2 = [6, 7, 8, 9]
numeros
[1, 2, 3, 4, 5]
numeros2
[6, 7, 8, 9]
lista_final = numeros + numeros2
lista_final
[1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros * 5
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 4, 5)
mi_tupla
(1, 2, 3, 4, 5)
#Aqui viene la diferencia con las lista, las tuplas:
mi_tupla.append(5)
#Error, 
# ya que la tuplas son un tipo de objeto estatico
# las listas son un tipo de objeto dinamico a 
# las cuales le podemos agregar y borrar 
# elementos a la tuplas no. Entonces cual es 
# la ventaja de usar tuplas y no lista, cuando 
# hacemos iteraciones(recoremos una lista con 
# un ciclo for podemos tener un ejecución más 
# rápida)
mi_tupla.pop(2)
#Error
# Pero si hacemos un for
for numero in mi_tupla:
...    print(numero)
...
1
2
3
4
5
# La diferencias con la listas es que el ciclo
# for funciona de una mejor manera con las tuplas.
# Las tuplas son la estructura más rapida que
# nosotros tenemos disponible dentro de python,
#  la diferencia con las listas es que las
#  podemos  modificar, las tuplas son inmutaples
# otro elemento inmutaples son los strings