

import streamlit as st

import pandas as pd

with st.echo(code_location='below'):

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

# Library
library(leaflet)
 
# load example data (Fiji Earthquakes) + keep only 100 first lines
data(quakes)
quakes =  head(quakes, 100)
 
# Create a color palette with handmade bins.
mybins=seq(4, 6.5, by=0.5)
mypalette = colorBin( palette="YlOrBr", domain=quakes$mag, na.color="transparent", bins=mybins)
 
# Prepare the text for the tooltip:
mytext=paste("Depth: ", quakes$depth, "<br/>", "Stations: ", quakes$stations, "<br/>", "Magnitude: ", quakes$mag, sep="") %>%
  lapply(htmltools::HTML)
 
# Final Map
leaflet(quakes) %>% 
  addTiles()  %>% 
  setView( lat=-27, lng=170 , zoom=4) %>%
  addProviderTiles("Esri.WorldImagery") %>%
  addCircles(~long, ~lat, 
    fillColor = ~mypalette(mag), fillOpacity = 0.7, color="white", radius=~sqrt(depth)*3000, stroke=FALSE, weight = 1,
    label = mytext,
    labelOptions = labelOptions( style = list("font-weight" = "normal", padding = "3px 8px"), textsize = "13px", direction = "auto")
  ) %>%
  addLegend( pal=mypalette, values=~mag, opacity=0.9, title = "Magnitude", position = "bottomright" )
