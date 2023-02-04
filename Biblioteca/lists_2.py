"""Ejercicios Listas
1.- Crea una lista llamada numeros que contenga los números del 1 al 10.
"""
numeros = [1,2,3,4,5,6,7,8,9,10]

"""
2.- Utiliza la función filter() para crear una nueva lista pares que contenga sólo los números pares de la lista numeros.
"""
filtrado = []

def par(numero):
    if(numero % 2 == 0):
        return True  
    return False

filtrado = filter(par,numeros)
lista_pares = list(filtrado)

print(lista_pares)

"""
3.- Utiliza la función map() para crear una nueva lista cuadrados que contenga el cuadrado de cada número en la lista numeros.
"""
def numeros_cuadrados(numero):
    return numero * numero
    
print(list(map(numeros_cuadrados, numeros)))

"""
4.- Utiliza la función reduce() para calcular la suma de todos los números en la lista numeros.
"""
from functools import reduce

def suma(numero1,numero2):
  return numero1 + numero2

print(reduce(suma, numeros))

"""
5.- Utiliza un ciclo for para imprimir cada elemento de la lista cuadrados junto con su índice en la lista.
"""
lista_cuadrados = list(map(numeros_cuadrados, numeros))

i = 1
for numeros in lista_cuadrados:
    print(i, numeros)    
    i += 1  
    
"""
6.- Utiliza un ciclo while para eliminar todos los números impares de la lista cuadrados.
"""

i=0
while i<len(numeros):
    if par(numeros[i]):
        numeros.pop(i)
    else:
        i +=1
    
print(numeros) 
"""
7.- Calcula con Python cuántos segundos han pasado desde la fecha de tu nacimiento.
"""
import datetime

[anio, mes, dia] = [2000, 1, 2]
fechaNacimiento = datetime.datetime(anio, mes, dia)
now = datetime.datetime.now()

totalSegNacimiento = (now - fechaNacimiento).total_seconds()
print(totalSegNacimiento)

"""
8.- Calcula con Python las fechas capicúa (palindromic number, por ejemplo: 2021-12-02) que ha habido desde la fecha de tu nacimiento hasta hoy.
"""

#Fecha actual
currentDate = datetime.datetime.now()

today = int(currentDate.strftime("%Y")+currentDate.strftime("%m")+currentDate.strftime("%d"))

birthday = 20000101
#Contador para la cantidad de capicuas
c=0

print("Los capicuas encontrados son los siguientes:")
for i in range(birthday,today+1):
    numSTR=str(i)
    numLista=list(numSTR)
    if numLista==numLista[::-1]:
        c+=1
        print(numSTR)
        
print("Total de Capicuas:",c)