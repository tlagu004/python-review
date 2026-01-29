import streamlit as st
import pandas as pd
import plotly.express as px
from apis import apod_generator
import os

st.balloons()
st.title("Hello world")
st.header("Internship Ready Software Development")
st.subheader("Prof. Gregory Reis")
st.divider()

# Load data
df = pd.read_csv("biscayneBay_waterquality.csv")

# Create the tabs
tab1, tab2, tab3, tab4 = st.tabs(
    ["Descriptive Stats", "2d Plots", "3d plots", "NASA's APOD"]
)

with tab1:
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Stats")
with tab2:
    # Changed "Temperature (C)" to "Temperature (c)"
    fig1 = px.line(df, x="Time", y="Temperature (c)")
    st.plotly_chart(fig1)
    
    # "ODO mg/L" and "pH" look correct based on your list
    fig2 = px.scatter(df, x="ODO mg/L", y="pH", color="pH")
    st.plotly_chart(fig2)

with tab3:
    # Changed "Total Water Column (m)" to "Total Water Column (m)" 
    # and ensured Latitude/Longitude are capitalized
    fig3 = px.scatter_3d(
        df, 
        x="Longitude", 
        y="Latitude", 
        z="Total Water Column (m)"
    )
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with tab4:
    st.header("NASA's Astronomy Picture of the Day")

    #TODO: call a function that generates the APOD
    url="https://api.nasa.gov/planetary/apod?api_key="
    response = apod_generator(url, os.getenv("NASA_API_KEY"))
    st.badge("Fetch Successful")
    print(response)

    # TODO: display the APOD image and title and other features
    st.subheader(response["title"])
    st.image(response["hdurl"])
    st.caption(response["explanation"])
    
 
