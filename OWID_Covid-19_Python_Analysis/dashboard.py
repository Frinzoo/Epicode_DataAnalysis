import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configurazione pagina ---
st.set_page_config(
    page_title="Dashboard COVID-19",
    page_icon="🦠",
    layout="wide"
)

# --- Caricamento dati (con cache per velocità) ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# --- Titolo ---
st.title("🦠 Analisi Diffusione COVID-19")
st.markdown("Dati: [Our World in Data](https://github.com/owid/covid-19-data)")

# --- Sidebar con filtri ---
st.sidebar.header("Filtri")

continenti = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
continente_sel = st.sidebar.multiselect(
    "Seleziona continenti", continenti, default=continenti
)

anno_sel = st.sidebar.selectbox("Anno", [2020, 2021, 2022, 2023], index=1)

nazioni_eu = ['Italy', 'Germany', 'France', 'Spain']
nazione_sel = st.sidebar.multiselect(
    "Nazioni europee", nazioni_eu, default=['Italy', 'France', 'Spain']
)

# --- KPI principali ---
col1, col2, col3 = st.columns(3)

# Casi mondiali totali
world_cases = df[df['location'] == 'World']['total_cases'].max()
col1.metric("🌍 Casi mondiali", f"{world_cases:,.0f}")

# Ospedalizzati 2021 (Italia)
hosp_ita = df[
    (df['location'] == 'Italy') &
    (df['date'].dt.year == 2021)
]['hosp_patients'].sum()
col2.metric("🏥 Ricoveri IT 2021", f"{hosp_ita:,.0f}")

# Totale decessi mondiali
world_deaths = df[df['location'] == 'World']['total_deaths'].max()
col3.metric("💀 Decessi mondiali", f"{world_deaths:,.0f}")

# --- Grafico casi per continente ---
st.subheader("Casi totali per continente")

ultimi_dati = (
    df[df['location'].isin(continenti)]
    .dropna(subset=['total_cases'])
    .groupby('location')
    .tail(1)
)
fig_bar = px.bar(
    ultimi_dati, x='location', y='total_cases',
    color='location', title="Casi totali per continente"
)
st.plotly_chart(fig_bar, use_container_width=True)

# --- Grafici affiancati ---
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Pazienti ospedalizzati 2021")
    hosp2021 = df[
        df['location'].isin(nazione_sel) &
        (df['date'].dt.year == anno_sel) &
        df['hosp_patients'].notna()
    ]
    fig_line = px.line(
        hosp2021, x='date', y='hosp_patients',
        color='location', title="Ospedalizzati nel tempo"
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col_b:
    st.subheader("Pazienti ICU 2021")
    icu2021 = df[
        df['location'].isin(nazione_sel) &
        (df['date'].dt.year == anno_sel) &
        df['icu_patients'].notna()
    ]
    fig_box = px.box(
        icu2021, x='location', y='icu_patients',
        color='location', title="Distribuzione ICU"
    )
    st.plotly_chart(fig_box, use_container_width=True)