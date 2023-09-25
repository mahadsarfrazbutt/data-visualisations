import plotly.express as px

df = px.data.gapminder().query("continent == 'Asia'")  # Get dataframe
print('dataframe created...')
print('visualizing...')

fig = px.bar(df, y='gdpPercap', x='country', title='Countries by GDP', text_auto='0.2s', animation_frame='year',
             animation_group='country', color='country', template='plotly_dark')  # Create figure
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2500  # Decrease animation speed

# fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,100)', 'paper_bgcolor': 'rgba(0,0,0,100)'}) --> Turns graph into terrible color

fig.show()
