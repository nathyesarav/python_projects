file = open("quijote.txt", encoding="UTF-8")
from sentiment_analysis_spanish import sentiment_analysis
sentiment = sentiment_analysis.SentimentAnalysisSpanish()

textQuijote = file.read()
palabras = textQuijote.split()
print(palabras[-1])
print(len(palabras)) 

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

print(sentiment.sentiment(textQuijote))
print(palabras.index("quijote"))
print(palabras[palabras.index("quijote")])