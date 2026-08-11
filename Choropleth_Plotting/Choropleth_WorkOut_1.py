import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd

df = pd.read_csv('./Choropleth_Plotting/2012_Election_Data')

print(df.shape)
print(df.info())
print(df.head())

data = dict(type= 'choropleth',
            colorscale='ylorrd',
            locations=df['State Abv'],
            locationmode = 'USA-states',
            z =df['Voting-Age Population (VAP)'],
            text= df['State'],
            colorbar={'title': '2012 Voting Age Population across States'},
            marker =dict(line=dict(width=2,color='rgb(12,12,12)')))


layout = dict(title = '2012 General Election Voting Data',
              geo = dict(scope='usa',showlakes = True,
                         lakecolor = 'rgb(85,173,240)'))

choromap = go.Figure(data=[data],layout=layout)

iplot(choromap)