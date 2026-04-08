# 🦠 COVID-19 Dashboard

Dashboard interattiva per l'analisi della diffusione del COVID-19 nel mondo, sviluppata come progetto d'esame del Master in Data Analysis @ **Epicode**.

---

## 🗂️ Struttura del progetto

```text
BW3/
├── api.py                  # API REST con FastAPI — espone i dati aggregati per continente
├── dash.html               # Dashboard interattiva (HTML + Plotly.js)
├── EsamePython.ipynb       # Notebook Jupyter con analisi esplorativa (EDA)
├── requirements.txt        # Dipendenze Python
├── .gitignore
└── README.md
```

> ℹ️ Il file `owid-covid-data.csv` **non è incluso** nel repository.  
> Non è necessario scaricarlo: sia `api.py` che `dash.html` recuperano i dati **automaticamente online** dall'URL ufficiale di Our World in Data.

---

## ⚙️ Installazione

### 1. Clona il repository

```bash
git clone https://github.com/Frinzoo/Epicode_DataAnalysis.git
cd Epicode_DataAnalysis/BW3
```

### 2. Installa le dipendenze

```bash
pip install -r requirements.txt
```

---

## 🚀 Avvio del progetto

La dashboard richiede **due server attivi contemporaneamente**.  
Apri due tab nel terminale:

**Tab 1 — API FastAPI (porta 8000):**
```bash
python -m uvicorn api:app --reload
```

**Tab 2 — Server HTTP per la dashboard (porta 8080):**
```bash
python -m http.server 8080
```

Poi apri nel browser:

```text
http://localhost:8080/dash.html
```

---

## 📊 Funzionalità principali

| Sezione | Descrizione |
|---|---|
| **Overview** | Grafico a donut con distribuzione dei casi totali per continente |
| **Paesi** | Grafico a torta interattivo (top 30 paesi) + tabella filtrabile per continente |
| **🇪🇺 Europa** | Trend mensili, ospedalizzati e ICU per Italia, Germania, Francia e Spagna |
| **Dataset** | Vista tabellare del dataset OWID filtrabile per anno e paese |

Caratteristiche aggiuntive:
- 🌙 Dark mode
- 📱 Layout responsive
- 🔢 KPI aggregati per continente
- ⚡ Dati aggiornati in tempo reale da OWID

---

## 🔌 API

L'API è costruita con **FastAPI** e recupera i dati direttamente online — nessun file locale necessario.

### Endpoint disponibile

| Metodo | Endpoint | Descrizione |
|---|---|---|
| `GET` | `/casi-continenti` | Restituisce i casi totali aggregati per continente in formato JSON |

**Esempio di risposta:**
```json
[
  { "location": "Europe", "total_cases": 245000000 },
  { "location": "Asia",   "total_cases": 310000000 }
]
```

Documentazione interattiva Swagger disponibile su:

```text
http://127.0.0.1:8000/docs
```

---

## 📓 Notebook di analisi

Il file `EsamePython.ipynb` contiene l'analisi esplorativa completa del dataset OWID:
- Caricamento e pulizia dei dati
- Analisi per continente e per paese
- Visualizzazioni con Pandas, Matplotlib e Seaborn
- Focus specifico sull'Europa (IT, DE, FR, ES)

---

## 📦 Dataset

I dati provengono da **Our World in Data (OWID)** e vengono recuperati automaticamente dal codice:

- 🔗 Repository: [owid/covid-19-data](https://github.com/owid/covid-19-data)
- 📄 Licenza: [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 🗓️ Copertura: gennaio 2020 — 2023

---

## 🛠️ Tecnologie utilizzate

| Categoria | Tecnologie |
|---|---|
| **Backend** | Python, FastAPI, Uvicorn |
| **Frontend** | HTML5, CSS3, JavaScript, Plotly.js |
| **Data Analysis** | Pandas, NumPy, Matplotlib, Seaborn |
| **Ambiente** | Jupyter Notebook / JupyterLab |

---

## 👤 Autore

**Francesco Laganà**  
Master in Data Analysis — Epicode  
📅 Aprile 2026