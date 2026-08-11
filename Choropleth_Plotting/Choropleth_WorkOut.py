import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd

df = pd.read_csv('./Choropleth_Plotting/2014_World_Power_Consumption')

print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

data = dict(type= 'choropleth',
            colorscale='ylorrd',
            locations=df['Country'],
            locationmode = "country names",
            z =df['Power Consumption KWH'],
            text= df['Country'],
            colorbar={'title': 'Power Consumptions of Countries in KWH'},
            marker =dict(line=dict(width=2,color='rgb(12,12,12)')))

layout=dict(title='2014 Gobal Power Consumption',
             geo=dict(showframe= True,projection={'type':'natural earth'}))

choromap = go.Figure(data=[data],layout=layout)
iplot(choromap)