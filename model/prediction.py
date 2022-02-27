import numpy as np

newdata = pd.DataFrame().reindex_like(df1)
newdata.fillna(value=0, inplace=True)
del newdata['std price']
newdata = newdata.iloc[[1]]

newdata['size'] = 21
newdata['kamers'] = 1
newdata['age'] = 7
newdata['nearby rating'] = 5
newdata['std distance1'] = 2

newdata

a = rf.predict(newdata)[0]

np.average(df[df['city'] == 'Amsterdam']['price'])*a