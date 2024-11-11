# scatter plot erzeugen
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt #for plotting

df = pd.read_csv('data/SynthData.csv', sep=',')

# spec 'a' darstellen
idx = df[df['spec']!='a'].index                  
df_a = df.drop(idx)  
ax1 = df_a.plot(kind='scatter', y='x1', x='x2', color='blue') 
plt.text(55,410, '(a)', size=10, color='blue')

# spec 'b' darstellen
idx = df[df['spec']!='b'].index                  
df_b = df.drop(idx)  
ax1 = df_b.plot(kind='scatter', y='x1', x='x2', color='green', ax=ax1) 
plt.text(55,320, '(b)', size=10, color='green')

# spec 'c' darstellen
idx = df[df['spec']!='c'].index                  
df_b = df.drop(idx)  
ax1 = df_b.plot(kind='scatter', y='x1', x='x2', color='orange', ax=ax1) 
plt.text(44,210, '(c)', size=10, color='orange')
plt.show()

# ---------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt #for plotting

df = pd.read_csv('data/SynthData.csv', sep=',')
idx = df[df['spec']!='a'].index                  
df_reg = df.drop(idx)                              # df_reg enthält nur spec 'a' 
print(df_reg)

# ---------------------------------------------------------------


# Species a --- lin. Regressionsmodell erzeugen
# ---------------------------------------------
import statsmodels.api as sm

x = df_reg['x2']           # unabhängige Variable
y = df_reg['x1']           # abhängige Variable

x = sm.add_constant(x)      # Offset in der lin. Regressionsgleichung zulassen

lin_reg_model = sm.OLS(y, x).fit()  # lin. Regressionsmodell anhand der Methode der minimalen Fehlerquadrate bilden
a = lin_reg_model.params.iloc[1]    # a: Gradient
b = lin_reg_model.params.iloc[0]    # b: Offset

print(lin_reg_model.summary())      # Modellgüte der OLS - Regression anzeigen
print()
print('----- Wichtige Modellparameter -----')
print('R2    : {:.3f}'.format(lin_reg_model.rsquared))  
print('adj.R2: {:.3f}'.format(lin_reg_model.rsquared_adj))
print('p     : {:.3f}'.format(lin_reg_model.f_pvalue))
print()
print('a     : {:.3f}'.format(a))
print('b     : {:.3f}'.format(b))


# ---------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np

# Messdaten darstellen
plt.scatter(df_reg['x2'], df_reg['x1'], color='purple')

# Regressionsgerade darstellen
plt.plot(df_reg['x2'], a*df_reg['x2']+b)

# Geradengleichung darstellen
plt.text(35, 450, 'x1 = ' + '{:.3f}'.format(b) + ' + {:.3f}'.format(a) + 'x2', size=12)

plt.xlabel('Parameter x2')
plt.ylabel('Parameter X1')
plt.show()

# ---------------------------------------------------------------


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# -------------------------------------------------------------------

# Logistische Regression anlernen für alle Species a, b, c
# -------------------------------------------------------------------

df = pd.read_csv('data/SynthData.csv', sep=',')
print(df.head())
print('\n ------------------------------------------------------------------------------------------\n')

mappings = {'a':1, 'b':2, 'c':3}
df['SpecNo'] = df['spec'].map(mappings)         # mittels Mapping für Species eine neue Spalte erzeugen

# Merkmale (Features) und Zielwert (Target) bereitstellen
X = df[['x1','x2']].to_numpy()
y = df['SpecNo']

# Trainingsdaten und Testdaten bereitstellen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

log_reg_classifier = LogisticRegression(random_state = 0)     # Klassifikator auf Basis logistischer Regression bereitstellen
log_reg_classifier.fit(X_train, y_train)                      # Klassifikator gemäß Daten parametrisieren

y_pred = log_reg_classifier.predict(X_test)                   # Klassifikator auf Testdaten anwenden

probs_y = log_reg_classifier.predict_proba(X_test)              # Wahrscheinlichkeiten für die Testdaten auslesen
probs_y = np.round(probs_y, 2)
#print(probs_y)
#input('Weiter')

# Ergebnistabelle der Klassifikationswahrscheinlichkeiten der Testdaten anzeigen
res = "{:<10} | {:<10} | {:<10} | {:<13} | {:<5}".format("y_test", "y_pred", "a(%)", "b(%)", "c(%)\n")
res += "-"*65+"\n"
res += "\n".join("{:<10} | {:<10} | {:<10} | {:<13} | {:<10}".format(x, y, int(a*100), int(b*100), int(c*100)) for x, y, a, b, c in zip(y_test, y_pred, probs_y[:,0], probs_y[:,1], probs_y[:,2]))
res += "\n"+"-"*65+"\n"
print(res)

# Konfusion-Matrix ausgeben
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Genauigkeit berechnen
accuracy = (cm[0][0] + cm[1][1]  + cm[2][2]) / (len(X_test))  # Genauigkeit berechnen
print('Genauigkeit:',accuracy)


# -------------------------------------------------------------------

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler       # für eine z-Scale Normalisierung
from sklearn.metrics import accuracy_score

df = pd.read_csv('data/SynthData.csv', sep=',')
print(df.head())
print('\n ------------------------------------------------------------------------------------------\n')

mappings = {'a':1, 'b':2, 'c':3}
df['SpecNo'] = df['spec'].map(mappings)         # mittels Mapping für Species eine neue Spalte erzeugen

# Merkmale (Features) und Zielwert (Target) bereitstellen
X = df[['x1','x2']].to_numpy()
y = df['SpecNo']      #.to_numpy()

# ---------------------------------------------------------------
# kNN-Klassifikation anlernen
# ---------------------------------------------------------------

# Aufteilung des Datensatzes in Trainingsdaten und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, # Samples/Proben/Beispiele/DatenPunkte
                                                    y, # Labels/Klassifikation
                                                    train_size = 0.75,   # Anteil der Trainingsdaten aus X,y
                                                    test_size = 0.25,    # Anteil der Testdaten aus X,y
                                                    random_state = 2)    # Zufallsinit. für reproduzierbare Ergebnisse

# --- der Normalisierer ermöglicht bessere Ergebnisse ???
#scaler = StandardScaler()                  # Standard-Normalisierer
#X_train = scaler.fit_transform(X_train)    # transformieren der Trainingsdaten
#X_test = scaler.transform(X_test)          # transformieren der Testdaten





# --- Datensatz einteilen ---
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

# --- guten k-Wert bestimmen ---
accuracy = []
for i in np.arange(1, 20):#101):
    new_model = KNeighborsClassifier(n_neighbors = i)
    new_model.fit(X_train, y_train)
    new_predictions = new_model.predict(X_test)
    accuracy.append(accuracy_score(y_test, new_predictions))

# Ergebnis anzeigen
plt.figure(figsize = (5,3))
plt.plot(accuracy)  
plt.ylim(0.75, 1.0) 
plt.xlabel('Neighbours')
plt.ylabel('Accuracy')
plt.show()


# -------------------------------------------------------------------


# Klassifikatoren erzeugen
knn4 = KNeighborsClassifier(n_neighbors = 4)   # KNN-Klassifikator für unter Nutzung der jeweils 4

# Klassifikatoren anlernen - unter Nutzung der Trainingsdaten
knn4.fit(X_train, y_train)


# Klassifikatoren arbeiten lassen - unter Nutzung der Testdaten
y_pred_4 = knn4.predict(X_test)

# Ergebnisgüte bestimmen
from sklearn.metrics import accuracy_score
print("Accuracy with k=4", accuracy_score(y_test, y_pred_4))



# -------------------------------------------------------------------


# ----- Live-Klassifikation -----
print('used mapping:',mappings)
while True:
    x1_in = int(input('x1 (200...450): '))     
    x2_in = int(input('x2 (35...55): '))       
    if x1_in<0 or x2_in<0:
        break                                        # Schleifenende >>> Programmende
    X_live = [[x1_in, x2_in]]                        # Merkmale der Live-Daten
    y_pred_live = log_reg_classifier.predict(X_live) # Vorhersage/Klassifikation gemäß oben angelerntem Modell vornehmen
    print('Prediction:',y_pred_live)                 # Ergebnis anzeigen

