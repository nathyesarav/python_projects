#Clase 1 Proyecto: Definidendo la aventura

#Equipamiento - Costo en monedas trekjuls
print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

mapa = 70.67
botas = 120.23
bateria = 11.69
linterna = 28
agua = 73
botella = 20.5
snacks = 8.8
brujula = 60.99
reloj = 83.75
lentes_sol = 53.28


print("Lista tres objetos del equipamiento: Nombre y valor")
print("botella", botella)
print("agua", agua)
print("snacks", snacks)


#Operadores
print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

agua_en_botella = agua + botella
linterna_funcional = linterna + bateria

print("Agua en botella", agua_en_botella)
print("Linterna funcional", linterna_funcional)


print("¿El precio del agua en botella es menor al de la linterna funcional?")
print(agua_en_botella < linterna_funcional)

print("¿Cuanto valdría comprar unos snacks y una brujula?")
print(snacks + brujula)

print("¿Si tengo 100 puntos, me alcanza para comprar unas botas?")
print(botas <= 100)

#Clase 2 Proyecto: Tomando decisiones

print("No colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")

mochila = 0

if agua_en_botella + linterna_funcional + brujula + reloj + snacks <= 200:
    mochila = agua_en_botella + linterna_funcional + brujula + reloj + snacks
    print("El valor de los elementos es menor a 200: ", mochila)

elif agua_en_botella + linterna_funcional + brujula + reloj <= 200:
    mochila = agua_en_botella + linterna_funcional + brujula + reloj
    print("El valor de los elementos es menor a 200", mochila)

else:
    print("Ups! Ninguna de tus intentos fue exitoso")

if agua_en_botella + linterna_funcional + brujula <= 200:
    mochila = agua_en_botella + linterna_funcional + brujula
    print("El valor de los elementos es menor a 200. Total compra: ", mochila)


#Ciclos

print ("Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")
mochila_dos = 0

while (mochila_dos <= 200):
    mochila_dos += agua_en_botella
    print("Mochila dos: ", mochila_dos)

mochila_dos -= agua_en_botella
print("Nos pasamos, vamos a restar una botella de agua, ahora tenemos: ", mochila_dos)

#Clase 3 Proyecto: 

#Diccionarios
print("La esfingue le hizo una actualización a tu mochila, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")

mochila_actualizada = {
    "agua_en_botella" : {"cantidad": 1, "valor_unitario": agua_en_botella},
    "linterna_funcional" : {"cantidad": 1, "valor_unitario": linterna_funcional},
    "brujula" : {"cantidad": 1, "valor_unitario": brujula}
}

mochila_dos_actualizada = {
    "agua_en_botella" : {"cantidad": 2, "valor_unitario": agua_en_botella}
}

#Listas

print("En esta aventura te van a acompañar 8 integrantes más, y te han pedido que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")

vehiculo = [{}] * 7

for compartimiento in range(7):
    vehiculo[compartimiento] = {
        "agua_en_botella" : {"cantidad": 1, "valor_unitario": agua_en_botella},
        "linterna_funcional" : {"cantidad": 1, "valor_unitario": linterna_funcional},
        "brujula" : {"cantidad": 1, "valor_unitario": brujula}
    }
    print("Acabas de armar la mochila para el compartimiento: ", compartimiento + 1)


for mochila in vehiculo:
    print(mochila)

#Clase 4 Proyecto:

print("La esfinge te pide que para cuatro integrantes se recolecten 3 elementos sin importar las cantidades y te da las siguientes opciones: brujula, linterna_funcional, snacks y agua_en_botella")
print("Ademas te va a pedir calcular el total de elementos que hay en tu equipo")
#Agregamos 2 snacks, 2 brujulas y una linterna funcional para los 4 primeros integrantes


def agregarElementosAMochilas():
    for compartimiento in range(3):
        vehiculo[compartimiento] = {
            "agua_en_botella" : {"cantidad": 1, "valor_unitario": agua_en_botella},
            "linterna_funcional" : {"cantidad": 2, "valor_unitario": linterna_funcional},
            "brujula" : {"cantidad": 3, "valor_unitario": brujula},
            "snacks" : {"cantidad": 2, "valor_unitario": snacks},
        }
    imprimir(vehiculo)
    calcularTotalElementosEnMochilas(vehiculo)

def calcularTotalElementosEnMochilas(vehiculo):
    total_elementos_mochilas = {}
    
    print("Calculo elementos en mochila")
    for mochila in vehiculo: 
        for elemento, detalle in mochila.items(): 
            if elemento in total_elementos_mochilas:
                total_elementos_mochilas[elemento] += detalle["cantidad"]
            else:
                total_elementos_mochilas[elemento] = detalle["cantidad"]

    print(total_elementos_mochilas)


def imprimir(estructura):
    for objeto in estructura:
        print(objeto)

agregarElementosAMochilas()

