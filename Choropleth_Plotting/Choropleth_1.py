import plotly as py
import plotly.io as pio
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#init_notebook_mode(connected=True)

data = dict(type='choropleth',
            locations=['AZ','CA','NY'],
            locationmode='USA-states',
            colorscale='Portland',
            text = ['text 1','text 2', 'text 3'],
            z =[1.0,2.0,3.0],
            colorbar = {'title': 'Colorbar Title Goes Here'})

layout = dict(geo = {'scope': 'usa'})

choromap = go.Figure(data=[data], layout= layout)

iplot(choromap)
#choromap.show(renderer='vscode')
#print(pio.renderers)