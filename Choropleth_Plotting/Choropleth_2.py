import plotly as py
import plotly.io as pio
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Choropleth_Plotting/2011_US_AGRI_Exports')

print(df.shape)
print(df.info())
print(df.columns)

data = dict(type='choropleth',
            colorscale= 'ylorrd',
            locations = df['code'],
            locationmode = 'USA-states',
            z = df['total exports'],
            text = df['text'],
            marker = dict(line = dict(color = 'rgb(12,12,12)',width= 2)),
            colorbar = {'title': 'Millions USD'})

layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope='usa',showlakes=True, lakecolor='rgb(85,173,240)'))

choromap = go.Figure(data=[data],layout=layout)

iplot(choromap)