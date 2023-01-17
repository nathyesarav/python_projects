file = open("quijote.txt", encoding="UTF-8")
textQuijote = file.read()
#print(textQuijote)
palabras = textQuijote.split()
#print(palabras[0])
#print(len(palabras)) 
#frases = textQuijote.splitlines()
#print(len(frases))

def mayor(palabras):
    max = palabras[0]
    for x in palabras:
        if len(x) > len(max):
            max = x;
    return max       

def main(palabras):
    print ("La palabra con mayor número es: ", mayor(palabras))    
    print("La cantidad de la palabra con mayor número es: ", len(mayor(palabras)))    

main(palabras);