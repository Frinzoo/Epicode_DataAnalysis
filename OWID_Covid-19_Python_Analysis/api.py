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

@app.get("/casi-continenti")
def casi_continenti():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    continenti = ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]
    ultimi = (
        df[df["location"].isin(continenti)]
        .dropna(subset=["total_cases"])
        .groupby("location")
        .tail(1)[["location", "total_cases"]]
    )
    return ultimi.to_dict(orient="records")
