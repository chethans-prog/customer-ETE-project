import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import standardsccalar
from tensorflow.keras import sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import Earlystopping
from tensorflow.keras.models import load_model

df = pd.read_csv('bank_churn_data - bank_churn_data')

x = df.drop(['Customerid','Surname','Exited'], axis=1)
y = df['Exited']

x['Geography'] = LableEncoder().fit_transform(x['Geography'])
x['Gender'] = LableEncoder().fit_transform(x['Gender'])

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
scaler = StandardScalar()
x_train = scaler.fit
