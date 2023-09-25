"""Open-Street Map mode"""
import pandas as pd
import plotly.express as px

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")  # Get the data

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["blue"], zoom=3, height=800, size='Population',
                        title='Population of US cities(Size corresponds to population)')  # Make the figure
fig.update_layout(mapbox_style="open-street-map")  # Set view mode
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})  # Set margins
fig.show()
