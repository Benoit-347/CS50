import requests

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

# 2. Fetch a reliable World GeoJSON directly from Folium's official repository
world_geo_url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
print("Downloading World GeoJSON data...")
response = requests.get(world_geo_url)
json_data = response.json()

# 3. Create the Choropleth layer
# Notice that key_on is now 'feature.properties.name' to match this specific JSON
choropleth = folium.Choropleth(
    geo_data=json_data,
    data=total_df,
    columns=(total_df.index, 'total_vaccinations_per_hundred'),
    key_on='feature.properties.name', 
    fill_color='RdYlGn',
    fill_opacity=0.7,
    line_opacity=0.5,
    nan_fill_color='white',             
    legend_name="Total Vaccinations per Hundred"
).add_to(world_map)

# 4. Add interactive hover tooltips
# Notice that fields is now ['name'] to match the GeoJSON
folium.GeoJson(
    json_data,
    style_function=lambda x: {'fillColor': 'transparent', 'color': 'transparent'},
    tooltip=folium.GeoJsonTooltip(
        fields=['name'], 
        aliases=['Country:'],
        localize=True
    )
).add_to(world_map)

folium.LayerControl().add_to(world_map)

# 5. Save the map to an interactive HTML file
output_file = "global_vaccination_map.html"
world_map.save(output_file)
print(f"Success! The map has been generated and saved to '{output_file}'.")
print("Open this file in your web browser to view the interactive map.")