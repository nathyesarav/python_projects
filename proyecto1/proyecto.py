import random
#Lista de opciones
opciones = ["piedra","papel","tijera"]

print("1:piedra\n2:papel\n3:tijera") 
#Inicialización de variables
opcion = 0
jugadas = 0
resultado = [0,0,0]
#Ciclo para limitar las jugadas
while jugadas < 5:
    #Ciclo para confirmar opciones válidas
    while opcion < 1 or opcion > 3:
        opcion = int(input("Elige una opcion\n"))
        if opcion < 1 or opcion > 3:
            print("Opcion no valida, elige nuevamente")
    print("Elegiste", opciones[opcion-1])
    #Pseudo random para la jugada del ordenador
    ordenador = random.randint(1,3)
    print("Ordenador elije", opciones[ordenador-1])

    if opcion == ordenador:
        resultado[0] = resultado[0] + 1
        print("Es un empate")
    elif opcion == ordenador+1 or opcion == ordenador-2: #Cálculo para las opciones de victoria
        resultado[1] = resultado[1] + 1
        print("Ganaste!")
    else:
        resultado[2] = resultado[2] + 1
        print("Perdiste! Gana ordenador")
    jugadas = jugadas + 1
    opcion = 0

print("Resultado final:\nEmpates:", resultado[0],"\nVictorias:", resultado[1],"\nDerrotas:", resultado[2])

if resultado[1] > resultado[2]:
    print("Ganaste!")
elif resultado[1] == resultado[2]:
    print("Es un empate!")
else:
    print("Perdiste, Gana el Ordenador!")
