import plotly.express as px

df = px.data.gapminder().query("continent=='Asia'")  # Get dataframe
print('dataframe created...')

# Add markers==True in attribute, but it looks hideous
fig = px.line(df, x='year', y='lifeExp', title='Life Expectancy of countries in Asia', color='country',  template='plotly_dark',
              hover_name='country', labels={'year': 'Year', 'lifeExp': 'Life Expectancy'})  # Create figure
fig.update_traces(line={'width': 3.5})  # Set line width
fig.show()
