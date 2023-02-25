file = open("quijote.txt", encoding="UTF-8")
texto = file.read()

# Creamos un string con los caracteres especiales que no deben tenerse en cuenta
limpiar = ",;:.¡!¿?-\"'"
for caracter in limpiar:
    texto = texto.replace(caracter, "")  # Remplazo los caracteres especiales por ""

texto = texto.replace("\n", " ")  # Reemplazo el salto de linea por " " para que no junte las palabras
texto = texto.lower()  # Se pasa el texto a minúsculas, para no tener palabras repetidas en el diccionario
palabras = texto.split(" ")  # Generamos una lista de palabras

# Contamos las palabras y las guardamos en un listado diccionario de palabras únicas
diccionario = {}
for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

#función para buscar la palabra con mayor frecuencia
def mayor(frecuencia):
    max = ''
    for x in frecuencia:
        if frecuencia[x] > frecuencia[max]:
            max = x;
    return max

def main(frecuencia):
    print ("La palabra con mayor número es: ", mayor(frecuencia), " con ", frecuencia[mayor(frecuencia)], "apariciones")  

#main(diccionario);

#Test2

from sentiment_analysis_spanish import sentiment_analysis
sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print(sentiment.sentiment("Me gusta la tombola"))

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    if(palabra == "que"):
        print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")

def mayor(frecuencia):
    max = frecuencia[0]
    for x in frecuencia:
        if len(x) > len(max):
            max = x;
    return max       

def main(frecuencia):
    print ("La palabra con mayor número es: ", mayor(frecuencia))    