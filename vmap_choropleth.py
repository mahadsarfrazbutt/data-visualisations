from urllib.request import urlopen
import pandas as pd
import json
import plotly.express as px

# Load json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)  # load coverts 'response' into proper format understood by python

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                 dtype={"fips": str})  # dtype converts fips code in dataset to string (fips is string in json)

fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp', color_continuous_scale="Viridis",
                    range_color=(0, 12), labels={'unemp': 'unemployment rate'}, scope="usa",
                    title='Unemployment Rates in US')  # Create figure
fig.show()
