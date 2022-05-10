import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

with st.echo(code_location='below'):

    import streamlit as st
    import folium
    import pandas as pd


    def print_hello(name = "World"):
        st.write(f"## Hello, {name}!")

    name = st.text_area("enter your name")
    print_hello(name)

    @st.cache
    def get_dataset():
        dataset_link = "metro_countries_total.csv"
        return pd.read_csv(dataset_link)

    dataset = get_dataset()

    dataset

    #from https://python-graph-gallery.com/313-bubble-map-with-folium

    m = folium.Map(location=[0,0])

    m
