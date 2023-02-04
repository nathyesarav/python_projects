#Ejercicio de Listas 3

#1.- Escribe una función que extraiga de una lista de números el menor y el mayor.
def MaxMin(lista):
    lista.sort()
    min = lista[0]
    max = lista[-1]
    newList = [min, max]
    return newList

#2.- Escribe otra función que haga de test de la primera con los siguientes casos:
#La función de test dará un ok por cada respuesta correcta y un fail en caso contrario.

def test():
    if MaxMin([1,2,3,4,5,6,7,8,9]) == [1,9]:
        print("ok")
    else:
        print("fail")

    if MaxMin([9,8,7,6,5,4,3,2,1]) == [1,9]:
        print("ok")
    else:
        print("fail")
    
    if MaxMin([0,-1,9,-12]) == [-12,9]:
        print("ok")
    else:
        print("fail")

    if MaxMin([0,0,0]) == [0,0]:
        print("ok")
    else:
        print("fail")    

    if MaxMin([-1]) == [-1,-1]:
        print("ok")
    else:
        print("fail")

    if MaxMin([]) == []:
        print("ok")
    else:
        print("fail")    

#3.- Escribe una función que sume los números de una lista.

def suma(lista):
    sumaLista = sum(lista)
    return sumaLista

#4.- Escribe su función de test

def testSum():
    testList = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]
    listSum = sum(testList)
    print(listSum)
testSum()    