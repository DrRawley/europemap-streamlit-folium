import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

# # center on Liberty Bell, add marker
# m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
# folium.Marker(
#     [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
# ).add_to(m)

# # call to render Folium map in Streamlit
# st_data = st_folium(m, width=725)

df = pd.read_csv('europe.csv')

m   = folium.Map(location=[54.91, 25.32], zoom=5)

for row in df:
  folium.Marker(
    [row['Latitude'], row['Longitude']], tooltip=row['Country'], popup=row['Country']
  ).add_to(m)

st_data = st_folium(m, width=800)

st.text(df)









# """
# # Welcome to Streamlit!
# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).
# """
# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))
