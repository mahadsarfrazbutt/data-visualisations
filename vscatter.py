import plotly.express as px

df = px.data.gapminder()
print('dataframe created...')
print('visualizing...')

# log_x attribute affects the x-axis by making it non-linear so that the bubbles stay in appropriate position
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country', size_max=150,
                 animation_frame='year', animation_group='gdpPercap', log_x=True, range_x=[100, 100000], range_y=[25, 90])
fig.update_layout(
    title=dict(text="GDP per capita compared to life Expectancy and Population", font=dict(size=20), automargin=True,
               yref='paper', xref='paper'))
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2500  # Decrease animation rate
fig.show()
