import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

dates = pd.date_range(start='1/1/2000', end='12/31/2030')

df = pd.DataFrame()
df['day'] = dates.day
df['month'] = dates.month
df['year'] = dates.year

df['weekday'] = dates.dayofweek

weekday_map = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

X = df[['day', 'month', 'year']]
y = df['weekday']

model = DecisionTreeClassifier()
model.fit(X, y)

with open('day_predictor.pkl', 'wb') as f:
    pickle.dump((model, weekday_map), f)

print("Model trained and saved successfully as 'day_predictor.pkl'")
