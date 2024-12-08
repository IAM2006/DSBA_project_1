from sklearn import linear_model
import pandas as pd
import numpy as np
import json
import pickle
from random import randint

def predict(beds: float, baths: float, sqft: float, nb: int) -> float:
    global model
    try:
        p = float(model[nb][0].predict(np.array([[sqft]]))[0])
        p1 = float(model[nb][1].predict(np.array([[beds, baths]]))[0])
        return ((p * 0.9 + p1 * 0.1))
    except:
        return randint(30000000, 60000000) / 100


neighborhood_id = dict()
with open('neighborhood.pkl', 'rb') as f:
    neighborhood_id = pickle.load(f)
data = pd.read_csv("reviewed_dataset.csv")
train_dt = data.iloc[:4500, :]
test_dt = data.iloc[4500:, :]
train_d = dict()
mn = 100
for elem in list(neighborhood_id.keys())[1:]:
    if (train_dt[train_dt.neighborhood == neighborhood_id[elem]].shape[0] < 2):
        continue
    train_d[neighborhood_id[elem]] = train_dt[train_dt.neighborhood == neighborhood_id[elem]]
model = dict()
for elem in list(train_d.keys()):
    md = linear_model.LinearRegression()
    md1 = linear_model.LinearRegression()
    X_t = train_d[elem][['PROPERTYSQFT']]
    Y_t = train_d[elem][['PRICE']]
    X_t1 = train_d[elem][['BEDS', 'BATH']]
    Y_t1 = train_d[elem][['PRICE']]
    md.fit(X_t, Y_t)
    md1.fit(X_t1, Y_t1)
    model[elem] = (md, md1)