library(ggplot2)

#Importation du dataset
data<-read.csv("Housing.csv")

#Infos relative au dataset
head(data)
summary(data)

#Verifions les valeurs  manquantes
is.na(data)

#Vérifions les valeurs abberantes
ggplot(data, aes(y = price)) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "Box plot of Price", y = "Price") +
  theme_minimal()

#4 prix identifiés ayant des valeurs dont l'observations differe des autres observations mais vu le contexte de notre dataset on ne les consideras pas commme des valeurs abérrantes
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

#Histogramme de la colonne bedrooms
histogram_bedrooms <- ggplot(data, aes(x=bedrooms)) +
  geom_histogram(binwidth=1, fill="blue", color="black", alpha=0.9) +
  labs(title="Histogram de Bedrooms",
       x="Numbre de Bedrooms",
       y="Frequence")
print(histogram_bedrooms)
#la plupart des propriétés dans le dataset ont 2 ou 3 chambres, avec un pic notable à 3 chambres (environ 300 propriétés). Les maisons avec moins de 2 chambres ou plus de 4 chambres sont beaucoup moins fréquentes.
