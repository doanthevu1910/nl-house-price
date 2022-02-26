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

plt.figure()
plt.hist(df[df['city'] == 'Amsterdam']['distance1'])
# plt.xlabel('')
# plt.ylabel('')
# plt.title('')
# plt.legend()
plt.show()
# plt.close()

plt.figure()
plt.hist(df[df['city'] == 'Amsterdam']['price'], color='red', histtype='step')
plt.hist(df[df['city'] == 'Den Haag']['price'], color='green', histtype='step')
plt.hist(df[df['city'] == 'Eindhoven']['price'], color='blue', histtype='step')
plt.hist(df[df['city'] == 'Rotterdam']['price'], color='yellow', histtype='step')
plt.hist(df[df['city'] == 'Utrecht']['price'], color='purple', histtype='step')
# plt.xlabel('')
# plt.ylabel('')
# plt.title('')
plt.legend()
plt.show()
# plt.close()


