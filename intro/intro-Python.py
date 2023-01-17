# -*- coding: utf-8 -*-
"""Taller Practico Python.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1qlLv6qppkLDR8LYQuIDhnoTUH1Z1pwcX

# ¿Qué tipos de datos existen en python?
Por ahora nos concentraremos en los siguientes: String , Float, Integer, Boolean
String: lo utilizamos cuando queremos almacenar textos
tienen que estar dentro de comillas simples o dobles(' ' , " ")
"""
'hola que tal'
"hola que tal"

"""si es un número y está dentro de comillas, este será un string (no un número) 
"""
'3'
"""una forma de imprimir estos datos en nuestra consola es con "print"
"""
print('5')
print(type('5'))

"""# Int and Float
*   **Int**: son números enteros
*   **Float**: son números enteros pero con decimales
"""

print(type(5))
print(type(5.2))
print(5+5)
print("5"+"5")

"""# Booleanos: 
Pueden ser True o False, nos sirven para tomar decisiones binarias
"""

print(True)
print(False)

"""#Variables
¿Dónde podemos almacenar todos los datos?
Por ejemplo "emanuel"
Una variable es como una caja a la que le damos un nombre y nos permite almacenar información dentro, por ejemplo:
name = ”Emanuel”
se recomienda que los nombre de las variables sean cortos , en ingles y relacionado con su contenido / función 
"""
name='emanuel'
age=25
student=True

"""podemos llamar a la variables y ésta nos devolverá su contenido """
name

"""**importante**
recordar que el print , solo sirve para imprimir en consola la información... no se puede guardar una variable con print
"""
nuevoNombre=print('2')
type(nuevoNombre)

"""**Ejercicio rápido**
crear 3 variable que les pertiman almacenar:

*   Su nombre
*   Su edad
*   Si eres viajer@ frecuente o no
"""

"""# Tuplas y Listas
¿Qué pasa si queremos almacenar más de un dato dentro de una variable?
**Tuplas**: Nos permite almacenar varios datos dentro de unos paréntesis ( )
**Listas**: Lo mismo que las listas pero dentro de unos corchetes [ ]
"""

# Tupla
(3,'hola',5,True)
tupla=(3,'hola',5,True)
# Listas
[3,'hola',5,True]
lista=[3,'hola',5,True]

"""pero ¿Cómo puedo ingresar a un dato en particular?
solo basta con llamar a la tupla/lista y agregar el número del elemento entre corchetes
"""
# recordar que las listas y las tuplas empiezan a contar desde 0
tupla[0]

# si quiero contar la cantidad de elementos
len(tupla)

"""¿Cual es la diferencia entre una tupla y una lista? 
La **tupla** es inmutable , por ende siempre quedará igual.
En cambio en las **Listas** podemos agregar datos, eliminar datos y modificarlos
"""

lista.append("emanuel")
lista
tupla.append('emanuel')

"""**Ejercicio rápido**
1.   Crear una lista que contenga:
    Un String, Un Int y Un Booleano

lista=['hola',5,True]

2.   Llamar al 3er elemento de la lista
"""
lista=[2]

"""#Diccionario
Podemos almacenar un conjunto de datos, tal como las listas y las tuplas pero podemos decir que de una manera más ordenada, ya que los datos están vinculados con una key.
Por eso decimos que los diccionarios están estructurados como “Clave” “Valor”.
La forma de iniciar y finalizar un diccionario es con llaves {}
"""

{
    "nombre":"Emanuel",
    "edad":23,
    "viajero":True
}

#se pueden almacenar igual que las tuplas y listas dentro de una variable
miDiccionario={
    "nombre":"Emanuel",
    "edad":23,
    "viajero":True,
    "personajes":["Darsamat","elMago","JuanElGuerrero"]
}

# De esta manera si quiero acceder al nombre solo basta con llamar la variable y dentro de las llaves la key … de la siguiente manera
miDiccionario['nombre']

# en el caso de tener una lista dentro del diccionario, solo basta con iterarla igual que lo hariamos con una lista
miDiccionario['personajes'][0]

# accedo a las "keys"
miDiccionario.keys()

# accedo a los valores
miDiccionario.values()

# Puedo tener un diccionario dentro de otro diccionario
# puedo crear un diccionario dentro de otro diccionario
juego={
    "personajes":[
                    {"nombre":"Darsamat","tipo":"mago","level":23,"password":"320320"},
                    {"nombre":"JuanElGuerrero","tipo":"guerrero","level":22,"password":"13213123"},
                    {"nombre":"elMago","tipo":"elfo","level":24,"password":"32323213"},
                 ]
    }
#de esta manera tendremos varios personajes con varias cualidades

# en el caso de querer agregar una nueva Key
juego.update({"mundo":"la comarca","dia":"12/3/2021"})
juego.keys()

# en el caso de querer agregar más info dentro de una Key..
juego["personajes"].append({"nombre":"eliot","tipo":"arquero","level":12,"password":"04304304"})
juego["personajes"]

"""EJERCICIO

*   Crea tu propio personaje (agrega un personaje a "personajes")
juego["personajes"].append({"nombre":"nathye","tipo":"desing","level":110,"password":"12345678"})

# Condicionales
If , elif , else

Los utilizaremos para relizar condiciones. Si la condición se cumple se correra un codigo,
de no ser así se correra otro codigo
"""
ageEmanuel=30
ageJuan=35
agePedro=22

if ageEmanuel>ageJuan:
    print ('Emanuel es mayor que Juan')
else:
    print('Juan es mayor que Emanuel')

if ageEmanuel > 31:
    print('emanuel es mayor que 30')
elif ageJuan > 30:
    print('Juan es mayor que 30')
elif agePedro > 30:
    print ('Pedro es mayor que 30')
else:
    print('nadie es mayor que 30')

"""**Ejercicio**
Crear una condición que nos permita comparar el nivel de dos personajes
Pj1Level=23
Pj2Level=25
el mayor ganara la pelea (imprimir "personaje1" o "personaje2" ha ganado la pelea)
"""
Pj1Level=23
Pj2Level=25

if Pj2Leve2>Pj2Level:
  print('personaje2" ha ganado la pelea')
else:
  print('personaje1"ha gan ado la pelea')

"""# For Loops
Lo utilizaremos para recorrer una lista o tupla
La forma de escribir un for loop es la siguiente:
"""

for i in [2,"emanuel",True]:
    print(i)

# es lo mismo que 
names=[2,"emanuel",True]

for i in names:
    print(i)
"""**explicación**
"""

# analizaremos línea por línea , de arriba hacia abajo.
# en la primera línea “i” toma el valor del primer elemento de la lista.
# en este caso sería el 2 ..... luego baja al print e imprime el "i" (su valor es 2)
for i in [2,"emanuel",True]:
    print(i)
# vuelve a correr el loop y toma el valor de "emanuel"
# baja a la linea del print e imprime su valor (en este caso es "emanuel")
# y así hasta recorrer toda la lista
# Podríamos realizar operaciones dentro del loop , no sólo imprimir 
a=0

for i in names:
    a+=1
    if a>2:
      print("a ya es mayor a 2")
    # este loop se correra 3 veces ya que names tiene 3 elementos...
    # por lo que a “a” se le sumará 1 en la primera vuelta, en la segunda otro 1 y en la tercera otro 1 … quedando un valor de a=3 

a

# de la misma manera podría iterar un diccionario

juego={
    "personajes":[
                    {"nombre":"Darsamat","tipo":"mago","level":23,"password":"320320"},
                    {"nombre":"JuanElGuerrero","tipo":"guerrero","level":22,"password":"13213123"},
                    {"nombre":"elMago","tipo":"elfo","level":24,"password":"32323213"},
                 ]
    }

for i in juego['personajes']:
  print(i) #entonces i toma el valor de cada diccionario

for i in juego['personajes']:
  print(i['nombre'])

"""**Ejercicio**
Del diccionario anterior necesitamos imprimir el level de cada personaje
"""
for i in juego['personajes']:
  print(i['level'])

"""#While Loop
al igual que el For Loop este se repetira varias veces, pero solamente cuando su condición se cumpla (cuando sea True) .
Su forma de escribirlo es la suguiente:

```
while "condición que deseamos":
  codigo
```
de esta forma cada vez que la condición sea True, este while se volverá a correr
"""
a=0

while a < 2: #se correra hasta que a tome un valor mayor a 2 ... entonces la condición sera False y el while no correra
  a+=1
  print(a)

"""# Funciones
Utilizaremos bastante las funciones a la hora de escribir código ya que nos ayudar a no repetir siempre las mismas líneas de código
Su forma de declararlas es la siguiente
```
def nombre():
  codigo
```
luego llamaremos esta función para que corra el código que tiene dentro de la siguiente manera.
```
suma()
```
"""
def suma():
  total=2+2
  otracosa='lala'
  #agregaremos el "return" para indicar lo que queremos que nos devuelva
  return total
# llamamos la función
suma()
"""
**A su vez las funciones (como en matemáticas) están pensadas para introducir valores y poder realizar operaciones con estos valores**"""
def sumar(valor1,valor2):
  total=valor1+valor2
  return total

# introduciremos cualquier valor dentro de esta función
sumar(3,4)
# si recuerdan el append del diccionario, podríamos entonces convertirlo en una función
# juego["personajes"].append({"nombre":"eliot","tipo":"arquero","password":"04304304"})

existe=False

def registro(nombre,tipo,level,password):
  for i in juego['personajes']:
    print(i['nombre'])
    if i['nombre'] == nombre:
      existe=True
    else:
      existe=False

  if existe == True:
    return "personaje ya existe"
  else:
      juego['personajes'].append({"nombre":nombre,"tipo":tipo,"level":level,"password":password})
      return "personaje creado con exito"

registro("emaWar","Paladin",32,"2312312")
juego["personajes"]

"""**Ejercicio 1**
*   Crear una función que se llame "login".
Donde verifique si el nombre y la password coinciden, de ser así... ingresa
"""

def login(nombre,password):
  if i['nombre'] == nombre:
    if i['password'] == password:
      print("loguin exitoso")
  else:
    if i['nombre'] == nombre:
      if i['password'] != password:
        print("password incorrecto")
      else:
        print("nombre incorrecto")
        return login        

"""**Ejercicio 2**
*   Crear una función que se llame "batalla". 
Donde los dos valores a ingresar son personaje1 y personaje2... y el que tenga un level más alto gana
ayuda para el segundo ejercicio
```
def batalla(personaje1,personaje2):
"""
puntajeTotal= 0
puntos = 0

def batalla(personaje1,personaje2):
  if puntosP1 > puntosP2:
    puntajeTotal = puntosP1 + puntosP2
    print("el ganador es el personaje 1")
  else:
    if puntosP1 < puntosP2:
      puntajeTotal = puntosP1 + puntosP2
      print("el ganador es el personaje 2")
    else  
      print("es un empate")
      return batalla