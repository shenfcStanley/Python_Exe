import pickle
import numpy as np
import json

from sklearn.preprocessing import MinMaxScaler

encoding = 'utf-8'
str(b'hello', encoding)


#model = pickle.load(open('test_model', 'rb'))

model = pickle.loads(data)
#data = [1.6, 50.46, 45.79]
#data = [10, 20, 31]
#data = [162.89,23.89,46.92]
#data = [24.59, 24.61, 25]
data = [26.59, 23.61, 22]

# scaler = MinMaxScaler(feature_range=(0, 1))
# scaled_data = scaler.fit_transform(data_arr.reshape(1,-1))
# print(scaled_data)
# #data = [1.6, 50.46, 45.79]
# #data = [1, 2, 3]

data_arr = np.array(data).reshape(1,-1)
print(data_arr.shape)

y_hat = model.predict(data_arr)

print(y_hat)