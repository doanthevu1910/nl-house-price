import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
df.drop('year', 1)

citylist = ['Amsterdam', 'Den Haag', 'Eindhoven', 'Rotterdam', 'Utrecht']

frames = []

for cityname in citylist:
    city = df[df['city'] == cityname]

    city['std price'] = city['price'] / np.average(city['price'])

    city['std distance1'] = city['distance1'] / np.average(city['distance1'])

    frames.append(city)

result = pd.concat(frames)

result.to_csv('data/data1.csv', index=False)