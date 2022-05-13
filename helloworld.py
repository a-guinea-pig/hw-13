

import streamlit as st

import folium 

import pandas as pd

import matplotlib.pyplot as plt

from matplotlib.figure import Figure

with st.echo(code_location='below'):

    @st.cache
    def get_dataset(link):
        dataset_link = link
        return pd.read_csv(dataset_link)

    dataset_total = get_dataset("archive/metro_countries_total.csv")
    dataset_cities = get_dataset("archive/metro_countries_cities.csv")

    dataset_total_africa = dataset_total.loc[dataset_total['region'] == 'africa'] # 437C90
    dataset_total_asia = dataset_total.loc[dataset_total['region'] == 'asia'] # 255957
    dataset_total_australia = dataset_total.loc[dataset_total['region'] == 'australia'] # EDAFB8
    dataset_total_europe = dataset_total.loc[dataset_total['region'] == 'europe'] # A98743
    dataset_total_latin_america = dataset_total.loc[dataset_total['region'] == 'latin_america'] # F7C548
    dataset_total_north_america = dataset_total.loc[dataset_total['region'] == 'north_america'] # E54B4B

    dataset_total
    dataset_cities

    df = dataset_total[["inauguration", "region"]]

    df

    #распределение появления метро в странах по регионам

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
            start_decade_year = 1850 + (i*10)
            end_decade_year = 1850 + (i*10) + 10
            element = str(start_decade_year) + " - " + str(end_decade_year)
            decades.append(element)
        return decades

    decades_x = list_of_decades()
    constructed_by_decades_total = count_inaugurated_in_decades(dataset_total)

    axes_constructed_total = {'decade':decades_x,'metro systems inaugurated':constructed_by_decades_total}
    construction_data_total = pd.DataFrame(axes_constructed_total, columns=['decade','metro systems inaugurated'])

    fig_constructed_total = plt.figure(figsize=(14, 10))

    sns.barplot(
        y="decade",
        x="metro systems inaugurated",
        data=construction_data_total,
        estimator=sum,
        ci=None,
        color='#000F08');
    st.pyplot(fig_constructed_total)

    def choose_region_inauguration():
        st.header("how many countries opened metro in every decade in the particular region")
        sd = st.selectbox(
            "select a region",
            [
                "africa",
                "asia"
            ]
        )

        fig = plt.figure(figsize=(12, 6))

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

        st.pyplot(fig)

    choose_region_inauguration()
