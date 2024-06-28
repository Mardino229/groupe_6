import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("housing.csv")
data.head()

data.info()

data.isnull().sum()

doublons = data[data.duplicated()]
doublons.sum()

data.describe()

# Créer l'histogramme
plt.hist(data['bedrooms'], bins=10)
plt.xlabel('Nombre de chambres')
plt.ylabel('Fréquence')
plt.title('Histogramme des nombres de chambres')
plt.show()