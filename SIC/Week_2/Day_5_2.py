"""
# to use env variables in code: set API_KEY = "our_api_Key"
# os.getenv("API_KEY")

# Securely retrieve your key
api_key = os.getenv('API_KEY')

# URL format for Stamen Watercolor via Stadia Maps
# Note: Use {z}/{x}/{y}.jpg for watercolor tiles
tile_url = f"https://tiles.stadiamaps.com/tiles/stamen_watercolor/{{z}}/{{x}}/{{y}}.jpg?api_key={api_key}"
attribution = '&copy; <a href="" target="_blank">Stamen Design</a> &copy; <a href="https://stadiamaps.com" target="_blank">Stadia Maps</a>'

map = folium.Map(location = [37.2594750011864,127.05145091394964],
                 zoom_start=13,
                 tiles=tile_url, 
                 attr=attribution
                 )

"""

import numpy as np
import pandas as pd
import datetime
import json
import folium
from datetime import date, datetime, time, timezone
import matplotlib.pyplot as plt

# =====================================================================
# PART 1: Data Loading & Preprocessing
# =====================================================================
print("--- Loading and Cleaning COVID-19 Vaccination Data ---")

# 1. Load the dataset (Requires the file in the specific relative path)
df = pd.read_csv("./Data/covid-vaccination-doses-per-capita.csv")

# 2. Convert 'Day' from Object to Datetime, set it as index, and drop the original column
df['Date'] = pd.to_datetime(df['Day'])
df.set_index('Date', inplace=True)
df.drop(['Day'], axis=1, inplace=True)

# Check unique countries
num_countries = len(df['Entity'].unique())
print(f"Total unique countries in dataset: {num_countries}")

# 3. Group by Country ('Entity')
covid_c = df.groupby(['Entity'])

# (Optional Debugging) Loop through the group to see data distribution
# for key, group in covid_c:
#     print('+key:', key)
#     print('+number:', len(group))
#     print(group.head(), '\n')

# 4. Create a new dataframe with the sum of total vaccinations per hundred by country
total_df = covid_c[['total_vaccinations_per_hundred']].sum()
print("\nCumulative Vaccinations per Hundred (Top 5):")
print(total_df.head())


# =====================================================================
# PART 2: Folium Map Basics (Markers, Circles, and Tiles)
# =====================================================================
print("\n--- Generating Basic Folium Map Examples ---")

# 1. Basic map with specific tileset (Stamen Watercolor / Terrain)
# Note: Stamen tiles recently require API keys, so 'OpenStreetMap' or 'CartoDB positron' are safer defaults.
basic_map = folium.Map(location=[37.259475, 127.051450], zoom_start=13, tiles="OpenStreetMap")

# 2. Marker Map Example (Mt. Hood)
marker_map = folium.Map(location=[45.372, -121.6972], zoom_start=12)

# Adding standard markers
folium.Marker(
    location=[45.3288, -121.6625],
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud")
).add_to(marker_map)

folium.Marker(
    location=[45.3311, -121.7113],
    popup="Timberline Lodge",
    icon=folium.Icon(color="green")
).add_to(marker_map)

# Adding a Circle Marker
folium.CircleMarker(
    location=[45.3800, -121.6000],
    radius=100,
    popup="circle",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc"
).add_to(marker_map)


# =====================================================================
# PART 3: The US Unemployment Choropleth Example
# =====================================================================
print("--- Generating US Unemployment Choropleth ---")

url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)

us_map = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)"
).add_to(us_map)

folium.LayerControl().add_to(us_map)


# =====================================================================
# PART 4: Final Project - Global Covid-19 Vaccination Choropleth
# =====================================================================
print("--- Generating Global COVID-19 Vaccination Map ---")

# 1. Set global map center and boundary parameters
center = [35.762887, 84.083132]
world_map = folium.Map(
    location=center, 
    zoom_start=2,
    max_bounds=True,
    min_zoom=1, 
    min_lat=-84, max_lat=84, 
    min_lon=-175, max_lon=187
)

# 2. Load the GeoJSON boundary data for the world
# Make sure you have this GeoJSON file in your project directory
geo_path = "./Data/us-states.json"

try:
    with open(geo_path, encoding='utf-8') as f:
        json_data = json.load(f)
        
    # 3. Create the Choropleth layer
    choropleth = folium.Choropleth(
        geo_data=json_data,
        data=total_df,
        columns=(total_df.index, 'total_vaccinations_per_hundred'),
        key_on='feature.properties.COUNTRY', # Adjust this key to match your GeoJSON's exact property name
        fill_color='RdYlGn',
        fill_opacity=0.7,
        line_opacity=0.5,
        nan_fill_color='white',             # ENHANCEMENT: Handles countries with missing data
        legend_name="Total Vaccinations per Hundred"
    ).add_to(world_map)
    
    # ENHANCEMENT: Add interactive hover tooltips
    # This allows users to hover their mouse over a country and see its name.
    # Without this, choropleth maps are purely visual and lack precise numeric readouts.
    folium.GeoJson(
        json_data,
        style_function=lambda x: {'fillColor': 'transparent', 'color': 'transparent'},
        tooltip=folium.GeoJsonTooltip(
            fields=['COUNTRY'], # Must match the property in your GeoJSON
            aliases=['Country:'],
            localize=True
        )
    ).add_to(world_map)

    folium.LayerControl().add_to(world_map)

    # ENHANCEMENT: Save the map to an interactive HTML file
    # Simply calling `world_map` only works in a Jupyter Notebook. 
    # To use this in standard Python, you must save it to HTML and open it in a browser.
    output_file = "global_vaccination_map.html"
    world_map.save(output_file)
    print(f"Success! The map has been generated and saved to '{output_file}'.")
    print("Open this file in your web browser to view the interactive map.")

except FileNotFoundError:
    print(f"Error: Could not find the GeoJSON file at {geo_path}. Please ensure the directory structure is correct.")