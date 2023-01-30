# Ejercicio
# Crear una serie de tiempo con los siguientes 3 componentes:
# Tendencia Y0 = m * X + b, siendo M = 0.3 y b = 10
# Estacionalidad Y1 = sin(0.1 * X)
# Volatilidad Y2 = random, siendo random un número aleatorio (distribución, media y desviación a elegir)
# Dibuja en pantalla la serie de tiempo de los 100 primeros valores de X (entre 0 y 100)

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
m = 0.3
b = 10

# Tendencia lineal
X = np.arange(0, 100)
Y0 = m * X + b

# Estacionalidad
Y1 = np.10 * sin(0.1 * X)

# Volatilidad
np.random.seed(0)
Y2 = np.random.normal(0, 1, 100)

# Serie de tiempo total
Y = Y0 + Y1 + Y2

# Gráfica
plt.plot(X, Y)
plt.show()