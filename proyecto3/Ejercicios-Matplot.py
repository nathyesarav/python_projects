import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

"""Ejercicios Matplot
- Calcular el logaritmo decimal de 1, 10, 100, 1.000 y 10.000
- Crear un dataframe de 100 filas con 3 columnas: 
La primera llamada X contiene valores decimales incrementales del 1 al 10, 
por ejemplo: 1.0, 1.1, 1.2, 1.3, ...

```
La segunda columna llamada Y, contiene el valor Y = 3 + 5 * X
```
La tercera columna llamada log10Y contiene el logaritmo decimal de Y
- Representar gráficamente Y vs X
- Representar gráficamente log10Y vs X
- Representar gráficamente Y vs X forzando el eje Y a ser representado en escala logarítmica con la correspondiente función de matplotlib
```
"""
import math as ma

N=1
# Funcion para calcular logaritmos
def logaritmos():
    if N > 0:
        #resultado = math.log10(N)
        resultado = ma.log( N, 10 )
        print(resultado)   

logaritmos()

df = pd.DataFrame()

df['X'] = []
df['Y'] = []

