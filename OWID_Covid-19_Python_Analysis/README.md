# 🦠 COVID-19 Dashboard

Dashboard interattiva per l'analisi della diffusione del COVID-19 nel mondo, sviluppata come progetto d'esame del Master in Data Analysis @ **Epicode**.

---

## 📸 Anteprima

> Avvia la dashboard seguendo le istruzioni qui sotto e aprila su `http://localhost:8080/dash.html`

---

## 🗂️ Struttura del progetto

```text
BW3/
├── api.py
├── dash.html
├── EsamePython.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

> ⚠️ Il file `owid-covid-data.csv` non è incluso nel repository perché supera i limiti pratici di GitHub.  
> Va scaricato a parte e salvato nella root del progetto.

---

## ⚙️ Installazione

### 1. Clona il repository

```bash
git clone https://github.com/TUO_USERNAME/covid19-dashboard.git
cd covid19-dashboard
```

### 2. Installa i requirements

```bash
pip install -r requirements.txt
```

### 3. Scarica il dataset

Scarica il file CSV da Our World in Data e salvalo nella cartella del progetto come `owid-covid-data.csv`.

Link diretto:  
https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv

Oppure da terminale:

```bash
curl -L "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv" -o owid-covid-data.csv
```

---

## 🚀 Avvio del progetto

La dashboard richiede **due server attivi contemporaneamente**.

### Tab 1 — API FastAPI

```bash
python -m uvicorn api:app --reload
```

### Tab 2 — Server HTTP per la dashboard

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
| Overview | Grafico a donut con distribuzione dei casi totali per continente |
| Paesi | Grafico a torta interattivo + tabella filtrabile per continente |
| Europa | Trend mensili, ospedalizzati e ICU per Italia, Germania, Francia e Spagna |
| Dataset | Vista tabellare del dataset OWID filtrabile per anno e paese |

La dashboard include anche:
- Dark mode.
- Layout responsive.
- KPI iniziali per continente.
- API locale per i dati aggregati.

---

## 🔌 API

L'API è costruita con **FastAPI**.

### Endpoint disponibile

| Metodo | Endpoint | Descrizione |
|---|---|---|
| GET | `/casi-continenti` | Restituisce i casi totali aggregati per continente in formato JSON |

### Documentazione API

Quando l'API è attiva, puoi vedere la documentazione automatica qui:

```text
http://127.0.0.1:8000/docs
```

---

## 📓 Notebook di analisi

Il file `EsamePython.ipynb` contiene l'analisi esplorativa del dataset, con:
- caricamento e pulizia dati,
- analisi per continente,
- analisi per paese,
- focus sull'Europa,
- visualizzazioni e osservazioni.

---

## 📦 Dataset

Fonte dati: **Our World in Data (OWID)**

- Repository: https://github.com/owid/covid-19-data
- Dataset CSV: https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv
- Licenza: CC BY 4.0

---

## 🛠️ Tecnologie utilizzate

| Categoria | Tecnologie |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| Frontend | HTML, CSS, JavaScript, Plotly.js |
| Data Analysis | Pandas, NumPy, Matplotlib, Seaborn |
| Ambiente | Jupyter Notebook |

---

## 👤 Autore

**Francesco Laganà**  
Master in Data Analysis — Epicode  
Aprile 2026
