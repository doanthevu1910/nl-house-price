import pandas as pd

amsterdam = pd.read_csv('final/amsterdam2.csv')
amsterdam['city'] = 'Amsterdam'

denhaag = pd.read_csv('final/den-haag2.csv')
denhaag['city'] = 'Den Haag'

eindhoven = pd.read_csv('final/eindhoven2.csv')
eindhoven['city'] = 'Eindhoven'

rotterdam = pd.read_csv('final/rotterdam2.csv')
rotterdam['city'] = 'Rotterdam'

utrecht = pd.read_csv('final/utrecht2.csv')
utrecht['city'] = 'Utrecht'

frames = [amsterdam, denhaag, eindhoven, rotterdam, utrecht]
result = pd.concat(frames)

result.to_csv('data/data.csv', index=False)