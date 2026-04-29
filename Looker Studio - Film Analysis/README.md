import os
os.makedirs("/root/output", exist_ok=True)

readme = """# 🎬 Film Box Office Analysis

<div align="center">

![TMDB](https://img.shields.io/badge/Data-TMDB%20via%20Kaggle-01b4e4?style=flat-square&logo=themoviedatabase&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Tool-Looker%20Studio-4285F4?style=flat-square&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Pre--processing-Python%20%7C%20pandas-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

**Analisi esplorativa su budget, incassi, generi e paesi di produzione del cinema mondiale.**

[📊 Apri il Report](https://datastudio.google.com/u/0/reporting/6e9ff3e1-7115-46a9-b2c1-53e4e89f5eb9/page/p_o350xe352d?s=voSVWhiXX_I) ·[🗃️ Dataset Kaggle](https://www.kaggle.com/datasets/alanvourch/tmdb-movies-daily-updates)

</div>

---

## 📌 Overview

| Metrica | Valore |
|---|---|
| 🎬 Film analizzati | **12.359** |
| 💰 Budget totale | **$276.000.793.054** |
| 🎟️ Incassi totali | **$751.147.804.367** |
| 📈 ROI medio | **172,15%** |
| 🗓️ Copertura | **1910 – 2026** |
| 🌍 Paesi | **108** |
| 🎭 Generi | **20** |

---

## 🗂️ Struttura del Report

Il report è suddiviso in **6 pagine tematiche**, ognuna con filtri interattivi e un insight narrativo.

```
📊 Film Box Office Analysis
├── 1. Overview Generale        → KPI, scatter budget/incassi, mappa mondiale
├── 2. Cinema nel Tempo         → Trend per anno e decennio (film, incassi, popolarità)
├── 3. Budget vs Successo       → Top 10 per incassi e ROI, scatter per film
├── 4. Generi Cinematografici   → Distribuzione, budget/incassi/ROI per genere
├── 5. Produzione Globale       → Mappa coropleta, classifica 108 paesi
└── 6. Analisi Studios          → Top studios per volume e revenue, runtime vs incassi
```

---

## 📈 Insight Principali

> **1. Il decennio 2010 domina tutto.**  
> 3.771 film prodotti e $293 miliardi di incassi — il più produttivo e redditizio della storia.

> **2. Horror = ROI campione.**  
> Con soli $11,3M di budget medio e un ROI del **249%**, è il genere più efficiente economicamente.

> **3. Paranormal Activity batte Avatar.**  
> ROI di **1.288.938%** contro gli $2,9 miliardi di incasso assoluto di Avatar.

> **4. Adventure incassa il doppio dell'Action.**  
> $151M di incassi medi vs $97M, nonostante l'Action sia più prodotto.

> **5. USA = >50% della produzione mondiale.**  
> 6.587 film su ~12.000 totali provengono dagli Stati Uniti.

> **6. La durata ottimale è 108–150 minuti.**  
> I film in questo range hanno il miglior rapporto incasso/minutaggio.

---

## 🏆 Top Film

<details>
<summary><strong>Top 5 per Incassi Globali</strong></summary>

| # | Film | Incassi |
|---|---|---|
| 1 | Avatar | $2.923.706.026 |
| 2 | Avengers: Endgame | $2.799.439.100 |
| 3 | The Lion King | $2.425.476.380 |
| 4 | Avatar: The Way of Water | $2.353.096.253 |
| 5 | Titanic | $2.269.067.353 |

</details>

<details>
<summary><strong>Top 5 per ROI %</strong></summary>

| # | Film | ROI |
|---|---|---|
| 1 | Paranormal Activity | 1.288.938,67% |
| 2 | Nidja's Kitchen 2 | 499.900% |
| 3 | The Blair Witch Project | 414.298,5% |
| 4 | Someone Wants to Talk with You | 99.900% |
| 5 | Balasubas | 99.900% |

</details>

<details>
<summary><strong>Top 5 per Incasso/Minuto</strong></summary>

| # | Film | Incassi | Durata | $/min |
|---|---|---|---|---|
| 1 | Zootopia 2 | $1.868.208.796 | 108 min | $17.298.229 |
| 2 | Spider-Man: No Way Home | $1.921.847.111 | 148 min | $12.985.453 |
| 3 | The Avengers | $1.567.415.515 | 232 min | $11.167.154 |
| 4 | Interstellar | $746.606.706 | 169 min | $4.417.791 |

</details>

---

## 🎭 Generi — Budget, Incassi e ROI

| Genere | Film | Budget Medio | Incassi Medi | ROI |
|---|---|---|---|---|
| Drama | 3.123 | $13,1M | $29,9M | 128% |
| Comedy | 2.634 | $15,0M | $39,2M | 162% |
| Action | 1.723 | $36,0M | $97,2M | 170% |
| Horror | 845 | $11,3M | $39,5M | **249%** |
| Adventure | 627 | $47,4M | **$151,3M** | 219% |
| Crime | 557 | $18,4M | $36,5M | 98% |
| Thriller | 505 | $18,9M | $39,3M | 107% |

---

## 🌍 Top Paesi per Film Prodotti

| # | Paese | Film |
|---|---|---|
| 1 | 🇺🇸 United States of America | 6.587 |
| 2 | 🇬🇧 United Kingdom | 837 |
| 3 | 🇮🇳 India | 815 |
| 4 | 🇫🇷 France | 618 |
| 5 | 🇨🇦 Canada | 395 |
| 6 | 🇩🇪 Germany | 314 |
| 7 | 🇷🇺 Russia | 224 |

---

## 🏢 Studios — Volume vs Revenue

| Per N° Film Prodotti | Per Incassi Totali |
|---|---|
| Independent | Paramount Pictures |
| Paramount Pictures | Universal Pictures |
| Universal Pictures | Warner Bros. Pictures |
| Warner Bros. Pictures | Marvel Studios |
| Metro-Goldwyn-Mayer | Columbia Pictures |

---

## 📁 Struttura del Progetto

```
📦 Film-Box-Office-Analysis/
│
├── 📄 README.md
├── 📊 TMDB-DB.xlsx                   # Dataset ridotto (subset locale)
├── 📊 TMDB-final-clean.xlsx          # Dataset principale pulito
└── 📄 Film_Box_Office_Analysis.pdf   # Export statico del report Looker Studio
```

---

## 🛠️ Stack Tecnologico

| Tool | Utilizzo |
|---|---|
| ![Google Looker Studio](https://img.shields.io/badge/-Looker%20Studio-4285F4?style=flat-square&logo=google) | Report interattivo e visualizzazioni |
| ![Google Sheets](https://img.shields.io/badge/-Google%20Sheets-34A853?style=flat-square&logo=googlesheets&logoColor=white) | Storage dati e connessione a Looker |
| ![Python](https://img.shields.io/badge/-Python%20%7C%20pandas-3776AB?style=flat-square&logo=python&logoColor=white) | Pre-processing e pulizia dataset |
| ![Kaggle](https://img.shields.io/badge/-TMDB%20%2F%20Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white) | Fonte dati originale |

---

<div align="center">

Made with ❤️ by **Francesco Laganà** · Aprile 2026 · Master in Data Analysis @ Epicode

</div>
