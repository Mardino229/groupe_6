<<<<<<<< HEAD:Task_2/scatter.R
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

#nuages de points
scatter_plot <- ggplot(data, aes(x=area, y=price)) +
  geom_point(color="red", alpha=0.6) +
  labs(title="Scatter Plot de Area vs Price",
       x="Area (en pied carré)",
       y="Price (unités monétaires)")
print(scatter_plot)
#Le nuage de points indique que, bien que la taille de la propriété soit un facteur important pour déterminer le prix, d'autres variables jouent également un rôle significatif. Les prix des propriétés peuvent varier considérablement pour des surfaces similaires, et quelques propriétés de luxe ou dans des zones premium montrent des prix particulièrement élevés.
========
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

#nuages de points
scatter_plot <- ggplot(data, aes(x=area, y=price)) +
  geom_point(color="red", alpha=0.6) +
  labs(title="Scatter Plot de Area vs Price",
       x="Area (en pied carré)",
       y="Price (unités monétaires)")
print(scatter_plot)
#Le nuage de points indique que, bien que la taille de la propriété soit un facteur important pour déterminer le prix, d'autres variables jouent également un rôle significatif. Les prix des propriétés peuvent varier considérablement pour des surfaces similaires, et quelques propriétés de luxe ou dans des zones premium montrent des prix particulièrement élevés.
>>>>>>>> 1948c132fe393bd2bf4c301d4ce703751ff631aa:Tâche 2/scatter.R
