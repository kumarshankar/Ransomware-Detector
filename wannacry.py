# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 23:34:24 2018

@author: SHANKAR
"""

import numpy as np
import pandas as pd
from uszipcode import ZipcodeSearchEngine
from sklearn.metrics import mean_squared_error 
from sklearn.model_selection import cross_val_score 
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import time

#For Deep learning 
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential


add_train_prefix = lambda x: "C:\\Users\\SHANKAR\\Desktop\\Foundations of Algorithms Design and Machine Learning\\Project\\FADML_Project\\" + x
ransom_data = pd.read_csv(add_train_prefix("ransomware.txt"),sep=',',names=[ 'instructions','cache-references','cache-misses','branches','branch-misses'])
regular_data = pd.read_csv(add_train_prefix("regular.txt"),sep=',',names=[ 'instructions','cache-references','cache-misses','branches','branch-misses'])
spec_data = pd.read_csv(add_train_prefix("spec.txt"),sep=',',names=[ 'instructions','cache-references','cache-misses','branches','branch-misses'])


plt.plot(x=ransom_data.index.values,y=ransom_data.instructions)
plt.show()
sns.distplot(ransom_data.instructions, bins=100, kde=False, rug=True)

x=pd.DataFrame(np.zeros((50,5)))
m = ransom_data.index

for i in range(2335):
    if i <48:
        x.loc[i] = ransom_data.iloc[50*i,:]
    else:
        pass
    
    
def build_model(layers):
    model = Sequential()

    model.add(LSTM(
        input_shape=(layers[1], layers[0]),
        output_dim=layers[1],
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers[2],
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(
        output_dim=layers[3]))
    model.add(Activation("linear"))

    start = time.time()
    model.compile(loss="mse", optimizer="rmsprop")
    print("> Compilation Time : ", time.time() - start)
    return model

model = build_model([1, 2, 100, 1])
