import gmaps
import pandas as pd
from ipywidgets.embed import embed_minimal_html
import config

api_key = config.gmaps_api
df = pd.read_csv('data/data1.csv')

gmaps.configure(api_key=api_key)

fig = gmaps.figure()
heatmap_layer = gmaps.heatmap_layer(
  df[['latitude', 'longitude']],
  weights=df['price'],
  max_intensity=1000000,
  point_radius=5.0
)

fig.add_layer(heatmap_layer)
fig

embed_minimal_html('graphs/export.html', views=[fig])

#open html and save image, delete html afterwards