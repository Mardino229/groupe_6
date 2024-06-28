import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Task_2\housing.csv")
data.head()

data.info()

data.describe()

data.isnull().sum()

doublons = data[data.duplicated()]
doublons.sum()


plt.scatter(data['area'], data['price'])
plt.xlabel('Surface')
plt.ylabel('Prix')
plt.title('Graphique de dispersion des prix')
plt.show()