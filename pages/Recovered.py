import streamlit as st
import plotly.express as px
import pandas as pd


@st.cache_data
def load_data() -> pd.DataFrame:
    DATA_DIR = r"data\time_series_covid_19_recovered.csv"
    df = pd.read_csv(DATA_DIR)
    return df

@st.cache_data
def transform_data_for_scatter(df: pd.DataFrame) -> pd.DataFrame:
    df_sct = df.drop(columns=["Province/State", "Lat", "Long"])
    Lat_Long = df[["Country/Region", "Lat", "Long"]]
    df_sct = df_sct.groupby(by="Country/Region").sum(numeric_only=True)
    df_sct = df_sct.merge(right=Lat_Long, on="Country/Region", how="left")
    df_sct = df_sct.melt(id_vars=['Country/Region', 'Lat', 'Long'], value_name='Total Recovered', var_name='Date')
    return df_sct

df = load_data()
df_sct = transform_data_for_scatter(df=df)

st.markdown("# Analysis of Recovered")
st.write(
    """
    On this page, we provide visualizations like maps or barplot with respect to the total recoveries
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
        data=df_sct.loc[df_sct["Country/Region"].isin(country_select), ["Total Recovered", "Country/Region"]]\
            .groupby("Country/Region")\
                .max()\
                    .reset_index(),
        x="Country/Region",
        y="Total Recovered",
        color="#ff7744",
    )

barplot()

scatter_plot = px.scatter_map(
    data_frame=df_sct,
    lat="Lat",
    lon="Long",
    size="Total Recovered",
    size_max=100,
    color="Total Recovered",
    color_continuous_scale=px.colors.sequential.Oranges,
    hover_name="Country/Region",
    animation_frame="Date"
)

scatter_plot.update_layout(
        title = 'Recoveries by Covid-19',
)

st.button("Go To Time Lapse Map", on_click=scatter_plot.show, icon=":material/map:")