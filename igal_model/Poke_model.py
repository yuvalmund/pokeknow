# loading libraries
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

# loading training data
names = ['outdoorsi','social','happy','dark','intelligent','foodie','angry','gabay','pokemon']
dataset = pd.read_csv('pokemon_personalities.csv')

# split vector to features and lables
X = dataset.iloc[:, :-1].values.astype(float)
y = dataset.iloc[:, 8].values

from sklearn.neighbors import KNeighborsClassifier  
classifier = KNeighborsClassifier(n_neighbors=1)  
classifier.fit(X, y)

# we assume we already have oded's vector
#arr = [[8,10,10,2,6,8,2,0,"Coral"]]

# Prepare the DF we recieve from profiler
client_df = pd.DataFrame(data=ret_arr,columns=names)
client_X = client_df.iloc[:, :-1].values
client_Y = client_df.iloc[:, 8].values
client_X = client_X.astype(float)

# Predict!
final_pred = classifier.predict(client_X)[0]
final_pred