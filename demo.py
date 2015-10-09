import numpy as np
import cPickle
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

Features = np.load('Test_data5.npy')
Labels = np.load('Test_label5.npy')
model = RandomForestRegressor(n_estimators=200, max_features=(1/3.0))
with open('RandomModel.dat','rb') as f:
    model = cPickle.load(f)
mse = 0
scores = []
for i in xrange(len(Labels)):
    score = model.predict(Features[i])
    scores.append(score)
    mse = mse + ((Labels[i] - score)**2)/len(Labels)
print 'mse =',mse
plt.scatter(Labels, scores, s=0.1)