"""Produces a very ugly scatter_geo plot"""
import plotly.express as px

df = px.data.gapminder().query('year==2007')
print('dataframe created...')
print('visualizing...')

fig = px.scatter_geo(df, locations='iso_alpha', size='pop', hover_name='country', title='Cities by Population')  # Create map
fig.show()