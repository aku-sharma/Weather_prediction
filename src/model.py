import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data/data.csv")

X = data[['humidity', 'wind_speed', 'pressure']]
y = data['temperature']

model = LinearRegression()
model.fit(X, y)

def predict_temp(humidity, wind_speed, pressure):
    return model.predict([[humidity, wind_speed, pressure]])[0]