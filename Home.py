import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="Covid-19 Analysis",
    page_icon=":material/rocket:",
)

#pg = st.navigation(
#    pages=[
#        st.Page(Path(r".\pages\cases.py", title="Cases")),
#        st.Page(Path(r".\pages\deaths.py", title="Deaths")),
#        st.Page(Path(r".\pages\about.py", title="About", icon=":materials/question_mark:"))
#    ]
#)
#
#pg.run()

st.markdown("# Covid-19 Data Analysis")

st.subheader("This is a general analysis of deaths and infections of covid-19")
st.write(f"The dataset can be found in this URL: https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset?select=time_series_covid_19_confirmed.csv")

container_cols = st.columns(2)

container_cols[0].image(r"static\thumbs-novelcoronavirus.jpg")
container_cols[1].write(
    r"""
    COVID-19, covid, and incorrectly called coronavirus pneumonia is a disease 
    infection caused by SARS-CoV-2. The total number of deaths until 2024 according to (Hopkins, 2024)
    is 6,881,955 deaths, likewise, according to (Hopkins, 2024), as of 2023, there had been 
    administered a total of 13,338,833,198 vaccines.
    """
)
container_cols[0].write(
    r"""
    Produces symptoms including fever, cough, dyspnea (shortness of breath), myalgia (muscle pain)
    and fatigue. In severe cases, they are characterized by pneumonia, acute respiratory distress syndrome, 
    sepsis and circulatory shock. According to WHO estimates, in 2020, the infection was fatal among 
    0.5% and 1% of cases.
    """
)
container_cols[1].image(r"static\thumbs-novelcoronavirus.jpg")
st.subheader("References")
st.write(
    r"""
    \[1\] John Hopkins University of Medicine, CoronaVirus Resource Center: https://coronavirus.jhu.edu/map.html
    
    \[2\] Gorbalenya, A. E.; Baker, S. C.; el al. «Severe acute respiratory syndrome-related coronavirus: The species and its viruses – a statement of the Coronavirus Study Group». . doi:10.1101/2020.02.07.937862
    
    \[3\] Fox, Steven; Vashisht, Rishik; Siuba, Matthew; Dugar, Siddharth (July 17 2020). «Evaluation and management of shock in patients with COVID-19». Cleveland Clinic Journal of Medicine. ISSN 0891-1150. doi:10.3949/ccjm.87a.ccc052
    """
)