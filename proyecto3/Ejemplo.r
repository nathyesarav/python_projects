# Lenguaje R

# Crear dataframe con los datos X = [1, 2, 3, 4, 5, 6] e Y = [10, 4, 1, 2, 5, 11]
datos <- data.frame(X = c(1, 2, 3, 4, 5, 6), Y = c(10, 4, 1, 2, 5, 11))

# Dibujar con la función nativa de R
plot(datos)

# Dibujar con la librería ggplot2
library(ggplot2)
ggplot(data = datos) + geom_point(aes(x = X, y = Y))