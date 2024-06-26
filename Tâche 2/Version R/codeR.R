data<-read.csv("Housing.csv")
#Procedons d'abord au nettoyage de notre dataset
#Affichons les infos relative au dataset
head(data)
summary(data)
#verifions les valeurs  manquantes
is.na(data)
#Il n'y a aucune valeur manquantes
#véerifions les valeurs abberantes'
ggplot(data, aes(y = price)) +
geom_boxplot(fill = "lightblue") +
labs(title = "Box plot of Price", y = "Price") +
theme_minimal()
#j'ai identifier 4 prix ayant valeurs dont l'observations differe des autres observations mais vu le contexte de notre dataset je ne les considerais pas commme des valeurs abérrantes
ggplot(data, aes(y = area)) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "Box plot of area", y = "area") +
  theme_minimal()
#Pas de valeur abérrantes
ggplot(data, aes(y = bedrooms)) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "Box plot of bedrooms", y = "bedrooms") +
  theme_minimal()
ggplot(data, aes(y = bathrooms)) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "Box plot of bathrooms", y = "bathrooms") +
  theme_minimal()
ggplot(data, aes(y = stories)) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "Box plot of stories", y = "stories") +
  theme_minimal()
ggplot(data, aes(y = parking )) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "Box plot of parking ", y = "parking ") +
  theme_minimal()
#Visblement le dataset ne presente aucune anomalie
#Passon à l'histogramme de la colonne bedrooms
histogram_bedrooms <- ggplot(data, aes(x=bedrooms)) +
  geom_histogram(binwidth=1, fill="blue", color="black", alpha=0.9) +
  labs(title="Histogram de Bedrooms",
       x="Numbre de Bedrooms",
       y="Frequence")
print(histogram_bedrooms)
#la plupart des propriétés dans le dataset ont 2 ou 3 chambres, avec un pic notable à 3 chambres (environ 300 propriétés). Les maisons avec moins de 2 chambres ou plus de 4 chambres sont beaucoup moins fréquentes.
#nuages de points
scatter_plot <- ggplot(data, aes(x=area, y=price)) +
  geom_point(color="red", alpha=0.6) +
  labs(title="Scatter Plot de Area vs Price",
       x="Area (en pied carré)",
       y="Price (unités monétaires)")
print(scatter_plot)
#Le nuage de points indique que, bien que la taille de la propriété soit un facteur important pour déterminer le prix, d'autres variables jouent également un rôle significatif. Les prix des propriétés peuvent varier considérablement pour des surfaces similaires, et quelques propriétés de luxe ou dans des zones premium montrent des prix particulièrement élevés.


