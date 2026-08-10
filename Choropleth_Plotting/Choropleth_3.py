import plotly as py
import plotly.io as pio
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Choropleth_Plotting/2014_World_GDP')

print(df.shape)
print(df.info())
print(df.describe())
#print(df.isnull())

data = dict(type= 'choropleth',
            colorscale= 'ylorrd',
            locations=df['CODE'],
            z =df['GDP (BILLIONS)'],
            text = df['COUNTRY'],
            colorbar={'title': 'GDP of Countries in Billions'},
            marker =dict(line=dict(width=2,color='rgb(12,12,12)')))

layout =dict(title='2014 Gobal GDP',
             geo=dict(showframe= False,projection={'type':'natural earth'}))

choromap = go.Figure(data=[data],layout=layout)

iplot(choromap)