# Use the  well-trained model to predict the one-week peak load
import pandas as pd
import json
import csv
import numpy as np
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Dense

with open('model/my_model.json', 'r') as f:
    weights = json.load(f)

new_model = model_from_json(weights)
new_model.load_weights('model/my_model_weights.h5')

x_predict = [[1, 19, 25, 28700], [1, 20, 25, 28600], [0, 19, 24, 25700], [0, 19, 27, 24600], [0, 21, 28, 24300],[0, 21, 27, 24500], [1, 21, 28, 28500]]
x_predict = np.asarray(x_predict)
y_pred = new_model.predict(x_predict)

dates = ['20190402', '20190403', '20190404', '20190405', '20190406', '20190407', '20190408']

with open('submission.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    
    filewriter.writerow(['date', 'peak_load(MW)'])
    for i, j in zip(y_pred, dates):
        filewriter.writerow([j, i[0] + 17.416])

