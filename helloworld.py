import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import requests

### FROM: https://discuss.streamlit.io/t/ann-streamlit-folium-a-component-for-rendering-folium-maps/4367
from streamlit_folium import folium_static
import folium
### END FROM

st.set_page_config(layout="wide")

with st.echo(code_location='below'):
    
    @st.cache
    def get_dataset(link):
        dataset_link = link
        return pd.read_csv(dataset_link)


    dataset_total = get_dataset("metro_countries_total.csv")
    dataset_cities = get_dataset("metro_countries_cities.csv")

    dataset_total_africa = dataset_total.loc[dataset_total['region'] == 'africa']  # 437C90
    dataset_total_asia = dataset_total.loc[dataset_total['region'] == 'asia']  # 255957
    dataset_total_australia = dataset_total.loc[dataset_total['region'] == 'australia']  # EDAFB8
    dataset_total_europe = dataset_total.loc[dataset_total['region'] == 'europe']  # A98743
    dataset_total_latin_america = dataset_total.loc[dataset_total['region'] == 'latin_america']  # F7C548
    dataset_total_north_america = dataset_total.loc[dataset_total['region'] == 'north_america']  # E54B4B
    
    
    dataset_cities_africa = dataset_cities.loc[dataset_cities['region'] == 'africa']  # 437C90
    dataset_cities_asia = dataset_cities.loc[dataset_cities['region'] == 'asia']  # 255957
    dataset_cities_australia = dataset_cities.loc[dataset_cities['region'] == 'australia']  # EDAFB8
    dataset_cities_europe = dataset_cities.loc[dataset_cities['region'] == 'europe']  # A98743
    dataset_cities_latin_america = dataset_cities.loc[dataset_cities['region'] == 'latin_america']  # F7C548
    dataset_cities_north_america = dataset_cities.loc[dataset_cities['region'] == 'north_america']  # E54B4B

    # для посмотреть

    agree = st.checkbox('Show datasets')

    if agree:
         dataset_total
         dataset_cities    ;

    list_of_cities = dataset_cities['city'].tolist()

    # changes in database cities' names to find latitude and longitude of the cities properly
    list_of_cities[192] = "San Francisco"  # initial "San Francisco/Oakland"
    list_of_cities[95] = "Delhi"  # initial "Noida", new satellite city of Delhi


    # adding latitude and longitude of the cities for the map


    @st.cache
    def find_lat(c):
        entrypoint = "https://nominatim.openstreetmap.org/search"
        params1 = {'city': c,
                   "limit": 1,
                   'format': 'json'}
        r1 = requests.get(entrypoint, params=params1)
        data1 = r1.json()
        for item in data1:
            latitude1 = (float(item["lat"]))
        return latitude1


    list_of_la = []

    for i in list_of_cities:
        list_of_la.append(find_lat(i))


    @st.cache
    def find_lon(c):
        entrypoint = "https://nominatim.openstreetmap.org/search"
        params2 = {'city': c,
                   "limit": 1,
                   'format': 'json'}
        r2 = requests.get(entrypoint, params=params2)
        data2 = r2.json()
        for item in data2:
            longitude1 = (float(item["lon"]))
        return longitude1


    list_of_lo = []

    for i in list_of_cities:
        list_of_lo.append(find_lon(i))


    dataset_cities_with_la_lo = dataset_cities.copy()

    dataset_cities_with_la_lo["la"] = list_of_la
    dataset_cities_with_la_lo["lo"] = list_of_lo

    # palettes for seaborn

    main_palette_hex = ["#437C90", "#255957", "#EDAFB8", "#A98743", "#F7C548", "#E54B4B"]
    main_palette = sns.color_palette(main_palette_hex)


    # seaborn visualizations


    def count_inaugurated_in_decades(dataset):
        constructed = []
        for i in range(1, 18):
            start_year = 1850 + (i * 10)
            end_year = 1850 + (i * 10) + 10
            df1 = dataset[dataset['inauguration'].isin(range(start_year, end_year))]
            number_constructed = len(df1.index)
            constructed.append(number_constructed)
        return constructed


    def list_of_decades():
        decades = []
        for i in range(1, 18):
            start_decade_year = 1850 + (i * 10)
            end_decade_year = 1850 + (i * 10) + 10
            element = str(start_decade_year) + " - " + str(end_decade_year)
            decades.append(element)
        return decades


    # появление метро по странам

    col1, col2 = st.columns(2)
    with col1:
        st.header("Metro inauguration by countries")

        st.write("The following barplot shows when different countries inaugurated their first metro system."
                 "In most of countries that have metro systems they appeared in the second half of the 20th century.")

        decades_x = list_of_decades()
        constructed_by_decades_total = count_inaugurated_in_decades(dataset_total)

        axes_constructed_total = {'decade': decades_x, 'countries that inaugurated their first metro system': constructed_by_decades_total}
        construction_data_total = pd.DataFrame(axes_constructed_total, columns=['decade', 'metro systems inaugurated'])

        fig_constructed_total = plt.figure(figsize=(14, 10))

        sns.barplot(
            y="decade",
            x="metro systems inaugurated",
            data=construction_data_total,
            estimator=sum,
            ci=None,
            color='#000F08');
        st.pyplot(fig_constructed_total)

    with col2:
        st.header(" ")

        st.write("It is visible that in Asia and Latin America metro systems were inaugurated later than in Europe.")

        def choose_region_inauguration():
            sd = st.selectbox( label = "select a region", options = [ "africa", "asia", "australia", "europe", "latin america", "north america"])

            if sd == "africa":
                constructed_by_decades_africa = count_inaugurated_in_decades(dataset_total_africa)

                axes_constructed_africa = {'decade': decades_x, 'metro systems inaugurated': constructed_by_decades_africa}
                construction_data_total = pd.DataFrame(axes_constructed_africa, columns=['decade', 'metro systems inaugurated'])

                fig_constructed_africa = plt.figure(figsize=(14, 10))
                ax = sns.barplot(
                    y="decade",
                    x="metro systems inaugurated",
                    data=construction_data_total,
                    estimator=sum,
                    ci=None,
                    color='#437C90');

                ax.set(xlim=(0, 6))

                st.pyplot(fig_constructed_africa)

            elif sd == "asia":
                constructed_by_decades_asia = count_inaugurated_in_decades(dataset_total_asia)

                axes_constructed_asia = {'decade': decades_x, 'metro systems inaugurated': constructed_by_decades_asia}
                construction_data_total = pd.DataFrame(axes_constructed_asia, columns=['decade', 'metro systems inaugurated'])

                fig_constructed_asia = plt.figure(figsize=(14, 10))
                ax = sns.barplot(
                    y="decade",
                    x="metro systems inaugurated",
                    data=construction_data_total,
                    estimator=sum,
                    ci=None,
                    color='#255957');

                ax.set(xlim=(0, 6))

                st.pyplot(fig_constructed_asia)

            elif sd == "australia":
                constructed_by_decades_aus = count_inaugurated_in_decades(dataset_total_australia)

                axes_constructed_aus = {'decade': decades_x, 'metro systems inaugurated': constructed_by_decades_aus}
                construction_data_total = pd.DataFrame(axes_constructed_aus, columns=['decade', 'metro systems inaugurated'])

                fig_constructed_aus = plt.figure(figsize=(14, 10))
                ax = sns.barplot(
                    y="decade",
                    x="metro systems inaugurated",
                    data=construction_data_total,
                    estimator=sum,
                    ci=None,
                    color='#EDAFB8');

                ax.set(xlim=(0, 6))

                st.pyplot(fig_constructed_aus)

            elif sd == "europe":
                constructed_by_decades_eu = count_inaugurated_in_decades(dataset_total_europe)

                axes_constructed_eu = {'decade': decades_x, 'metro systems inaugurated': constructed_by_decades_eu}
                construction_data_total = pd.DataFrame(axes_constructed_eu, columns=['decade', 'metro systems inaugurated'])

                fig_constructed_eu = plt.figure(figsize=(14, 10))
                ax = sns.barplot(
                    y="decade",
                    x="metro systems inaugurated",
                    data=construction_data_total,
                    estimator=sum,
                    ci=None,
                    color='#A98743');

                ax.set(xlim=(0, 6))

                st.pyplot(fig_constructed_eu)

            elif sd == "latin america":
                constructed_by_decades_la = count_inaugurated_in_decades(dataset_total_latin_america)

                axes_constructed_la = {'decade': decades_x, 'metro systems inaugurated': constructed_by_decades_la}
                construction_data_total = pd.DataFrame(axes_constructed_la, columns=['decade', 'metro systems inaugurated'])

                fig_constructed_la = plt.figure(figsize=(14, 10))
                ax = sns.barplot(
                    y="decade",
                    x="metro systems inaugurated",
                    data=construction_data_total,
                    estimator=sum,
                    ci=None,
                    color='#F7C548');

                ax.set(xlim=(0, 6))

                st.pyplot(fig_constructed_la)

            elif sd == "north america":
                constructed_by_decades_na = count_inaugurated_in_decades(dataset_total_north_america)

                axes_constructed_na = {'decade': decades_x, 'metro systems inaugurated': constructed_by_decades_na}
                construction_data_total = pd.DataFrame(axes_constructed_na, columns=['decade', 'metro systems inaugurated'])

                fig_constructed_na = plt.figure(figsize=(14, 10))
                ax = sns.barplot(
                    y="decade",
                    x="metro systems inaugurated",
                    data=construction_data_total,
                    estimator=sum,
                    ci=None,
                    color='#E54B4B');

                ax.set(xlim=(0, 6))

                st.pyplot(fig_constructed_na)


        choose_region_inauguration()
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("How many metro systems were built, by decades")

        st.write("The following histogram shows the number of metro systems built (by cities in contrast to by countries"
                 "in the previous graphs). The dominance of Asian cities in the past years metro construction is seen clearly.")

        fig = plt.figure(figsize=(12, 6))
        sns.histplot(data=dataset_cities, x="year", hue="region",
                     fill=True, multiple="stack", palette=main_palette,
                     alpha=1, linewidth=0)

        st.pyplot(fig)

    # celluloid

    def count_inaugurated_in_5years(dataset):
        constructed = []
        for i in range(1, 28):
            end_year = 1890 + (i * 5)
            df1 = dataset[dataset['year'].isin(range(0, end_year))]
            number_constructed = len(df1.index)
            constructed.append(number_constructed)
        return constructed

    def list_of_5years():
        years5 = []
        for i in range(1, 28):
            start_decade_year = 1885 + (i * 5)
            end_decade_year = 1890 + (i * 5)
            element = str(start_decade_year) + " - " + str(end_decade_year)
            years5.append(element)
        return years5

    years5_x = list_of_5years()


    df = pd.DataFrame({ "africa": count_inaugurated_in_5years(dataset_cities_africa),
                       "asia": count_inaugurated_in_5years(dataset_cities_asia),
                       "australia": count_inaugurated_in_5years(dataset_cities_australia),
                       "europe": count_inaugurated_in_5years(dataset_cities_europe),
                       "latin america": count_inaugurated_in_5years(dataset_cities_latin_america),
                       "north america": count_inaugurated_in_5years(dataset_cities_north_america)},
                      index = years5_x)
    with col2:
        st.write("Let's take a closer look on the construstion of the Asian and European metro systems by 5-year intervals in the following animation.")

        ### FROM: https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-5.php, https://gist.github.com/ischurov/fb00906c5704ebdd56ff13d7e02583e4

        from celluloid import Camera
        import streamlit.components.v1 as components

        fig = plt.figure()
        camera = Camera(fig)
        for i in range(0, 28):
            df = pd.DataFrame({"europe": count_inaugurated_in_5years(dataset_cities_europe)[:i],
                               "asia": count_inaugurated_in_5years(dataset_cities_asia)[:i],},
                              index=years5_x[:i])
            x1 = df.index.values.tolist()
            y1 = df["europe"]
            x2 = df.index.values.tolist()
            y2 = df["asia"]
            plt.plot(x1, y1, label="europe")
            plt.plot(x2, y2, label="asia")
            plt.xticks([])
            plt.show()
            camera.snap()
        animation = camera.animate()

        components.html(animation.to_jshtml(), height=600)

        ### END FROM

    # folium

    st.header("Metro size by length")

    st.write("This bubble map allows to compare the length of metro systems around the world. The map is zoomable "
             "and the bubbles are signed with a city name.")

    length_map = folium.Map(location=[0, 0], tiles="OpenStreetMap", zoom_start=2)

    ### FROM: https://www.python-graph-gallery.com/313-bubble-map-with-folium

    for i in range(0, len(dataset_cities_with_la_lo)):
        folium.CircleMarker(
            location=[dataset_cities_with_la_lo.iloc[i]['la'], dataset_cities_with_la_lo.iloc[i]['lo']],
            popup=dataset_cities_with_la_lo.iloc[i]['city'],
            radius=float(dataset_cities_with_la_lo.iloc[i]['length_km']) / 100,
            color='crimson',
            fill=True,
            fill_color='crimson'
        ).add_to(length_map)

    folium_static(length_map)

    ### END FROM

    st.header("Metro size by annual ridership")

    st.write("Another way to compare the size of metro systems is their annual ridership. Apparently, the difference"
             "in annual ridership is less than in the total length.")

    ridership_map = folium.Map(location=[0, 0], tiles="OpenStreetMap", zoom_start=2)

    ### FROM: https://www.python-graph-gallery.com/313-bubble-map-with-folium

    for i in range(0, len(dataset_cities_with_la_lo)):
        folium.CircleMarker(
            location=[dataset_cities_with_la_lo.iloc[i]['la'], dataset_cities_with_la_lo.iloc[i]['lo']],
            popup=dataset_cities_with_la_lo.iloc[i]['city'],
            radius=float(dataset_cities_with_la_lo.iloc[i]['annual_ridership_mill']) / 100,
            color='crimson',
            fill=True,
            fill_color='crimson'
        ).add_to(ridership_map)

    folium_static(ridership_map)

    ### END FROM
