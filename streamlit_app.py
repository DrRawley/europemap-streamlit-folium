import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

"""
# European Map with Follium and Streamlit
[Daily Python Projects](https://dailypythonprojects.substack.com/)

[Dr. Rawley's Website](https://drrawley.com)
"""


df = pd.read_csv('europe.csv')

m   = folium.Map(location=[54.91, 25.32], zoom_start=3)

for _, row in df.iterrows():
  linkcountry = row['Country'].replace(" ", "_")
  linkhtml = f'<h1><a href="https://en.wikipedia.org/wiki/{linkcountry}">{row["Country"]}</a></h1>'
  folium.Marker(
    [row['Latitude'], row['Longitude']], tooltip=f"<h2>{row['Country']}</h2>", popup=linkhtml
  ).add_to(m)

st_data = st_folium(m, width=800)

for _, row in df.iterrows():
 text = f"[{row['Country']}](https://en.wikipedia.org/wiki/{row['Country'].replace(' ', '_')})"
 st.markdown(text)









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
