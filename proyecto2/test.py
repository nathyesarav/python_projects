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