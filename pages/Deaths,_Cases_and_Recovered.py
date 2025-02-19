import streamlit as st
import plotly.express as px
import pandas as pd
import functools


@st.cache_data
def load_data() -> pd.DataFrame:
    DATA_DIR_RECOV = r"data\time_series_covid_19_recovered.csv"
    DATA_DIR_DEATHS = r"data\time_series_covid_19_deaths.csv"
    DATA_DIR_CASES = r"data\time_series_covid_19_confirmed.csv"
    df_death = pd.read_csv(DATA_DIR_DEATHS)
    df_cases = pd.read_csv(DATA_DIR_CASES)
    df_recov = pd.read_csv(DATA_DIR_RECOV)
    return df_death, df_cases, df_recov

@st.cache_data
def transform_data_for_scatter(
    df_death: pd.DataFrame,
    df_cases: pd.DataFrame,
    df_recov: pd.DataFrame
) -> pd.DataFrame:
    
    @st.cache_data
    def transform_one_df_for_scatter(df: pd.DataFrame, col: str) -> pd.DataFrame:
        Lat_Long = df[["Country/Region", "Lat", "Long"]]
        df = df.drop(columns=["Province/State", "Lat", "Long"])
        df = df.groupby(by="Country/Region").sum(numeric_only=True)
        df = df.merge(right=Lat_Long, on="Country/Region", how="left")
        df = df.melt(id_vars=['Country/Region', 'Lat', 'Long'], value_name=col, var_name='Date')
        return df
    
    df_death, df_cases, df_recov = load_data()

    df_death = transform_one_df_for_scatter(df_death, "Total Deaths")
    df_cases = transform_one_df_for_scatter(df_cases, "Total Cases")
    df_recov = transform_one_df_for_scatter(df_recov, "Total Recovered")

    df_sct = df_death.merge(df_cases, how='inner', on=['Date', 'Country/Region', 'Lat', 'Long'])
    df_sct = df_sct.merge(df_recov, how='inner', on=['Date', 'Country/Region', 'Lat', 'Long'])

    return df_sct


df_death, df_cases, df_recov = load_data()

df_sct = transform_data_for_scatter(
    df_cases=df_cases,
    df_death=df_death,
    df_recov=df_recov
)

st.markdown("# Analysis of Cases, Recoveries and Deaths")
st.write(
    """
    On this page, we provide visualizations for total recoveries, deaths and cases
    of Covid-19 according to the data we have provided.
    """
)

view_data = st.checkbox("View Data", value=False)
if view_data:
    st.dataframe(df_sct.head(10))

country_select = st.multiselect(
    label="Select Countries to Compare",
    options=df_sct["Country/Region"].unique(),
    placeholder="Choose one or more",
    default="Spain"
)

st.subheader("Total Recoveries by Countries")

@st.fragment
def barplot():
    st.bar_chart(
        data=df_sct.loc[df_sct["Country/Region"].isin(country_select), ["Total Recovered", "Total Cases", "Total Deaths", "Country/Region"]]\
            .groupby("Country/Region")\
                .max()\
                    .reset_index(),
        x="Country/Region",
        y=["Total Recovered", "Total Cases", "Total Deaths"],
        color=["#ff7744", "#4477ff", "#77ff44"],
        stack=False
    )

barplot()