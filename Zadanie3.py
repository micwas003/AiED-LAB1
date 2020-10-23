import pandas as pd

print("W pierwszej kolejnosci ladujemy dane do analizy z plikow:")

pd_train = pd.read_csv("out/pd_train.csv", sep=";")
pd_test = pd.read_csv("out/pd_test.csv", sep=";")

print("Przeprowadzamy analize ilosciowa")

for zbior, nazwa_zbioru in [(pd_test, "Testowy Zbior"), (pd_train, "Treningowy Zbior")]:
    print("Analiza ilościowa dla:".format(nazwa_zbioru))
    for column in zbior.columns[1:]:
        print("Analiza dla etykiety:".format(column))
        print("Ilość wartości w zbiorze (per kolumna):".format(zbior.count()[column]))
        print("Ilość wartości unikatowych w zbiorze (per kolumna):".format(zbior[column].nunique()))
        print("Wartość średnia w zbiorze (per kolumna):".format(zbior[column].mean(axis=0)))
        print("Ilość wartości null w zbiorze (per kolumna):".format(zbior[column].isnull().sum()))
        print("Wartość maksymalna w zbiorze (per kolumna):".format(zbior[column].max()))
        print("Wartość minimalna w zbiorze (per kolumna):".format(zbior[column].min()))
        print("Wartość najczęściej występująca w zbiorze (per kolumna):".format(zbior[column].mode().max()))
        print("")
    print("")
