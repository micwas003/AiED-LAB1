from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd

print("W pierwszej kolejnosci ladujemy dane do analizy:")
wine_data = load_wine()

X_train, X_test = train_test_split(wine_data.data, train_size=0.6, shuffle=True)
y_train = Y_test = wine_data.feature_names

pd_train = pd.DataFrame(data=X_train, columns=y_train)
pd_test = pd.DataFrame(data=X_test, columns=Y_test)

print("Zapisujemy analize do plikow cvs z dokladnoscia do dwoch miejsc po przecinku:")
pd_train.to_csv("out/pd_train.csv", sep=";", float_format="%.2f", index=False)
pd_test.to_csv("out/pd_test.csv", sep=";", float_format="%.2f", index=False)
