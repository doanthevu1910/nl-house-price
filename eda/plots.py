import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/data1.csv')

plt.figure()
plt.hist(df[df['city'] == 'Amsterdam']['price'])
# plt.xlabel('')
# plt.ylabel('')
# plt.title('')
# plt.legend()
plt.show()
# plt.close()

plt.figure()
plt.hist(df[df['city'] == 'Amsterdam']['std price'])
# plt.xlabel('')
# plt.ylabel('')
# plt.title('')
# plt.legend()
plt.show()
# plt.close()