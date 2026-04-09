from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

URL = "https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/owid-covid-data.csv"
CONTINENTI = ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]

# Il CSV viene scaricato una sola volta all'avvio e salvato in memoria
_df_cache = None

def get_df():
    global _df_cache
    if _df_cache is None:
        print("Scaricamento CSV da OWID...")
        _df_cache = pd.read_csv(URL)
        print("CSV caricato in memoria.")
    return _df_cache

@app.on_event("startup")
async def startup_event():
    get_df()

@app.get("/casi-continenti")
def casi_continenti():
    df = get_df()
    ultimi = (
        df[df["location"].isin(CONTINENTI)]
        .dropna(subset=["total_cases"])
        .groupby("location")
        .tail(1)[["location", "total_cases"]]
    )
    return ultimi.to_dict(orient="records")