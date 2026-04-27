# Ecommerce Sales Analyzer

End-to-end data pipeline for the Brazilian Olist ecommerce dataset. Loads 9 raw CSVs, cleans and transforms the data with Pandas, loads into PostgreSQL, runs 7 analytical SQL queries, and generates Matplotlib charts.

## Stack

- Python 3.10
- Pandas
- PostgreSQL + SQLAlchemy
- Matplotlib

## Dataset

[Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — ~100k orders across 9 CSV files covering customers, orders, products, sellers, payments and reviews.

## Project Structure

```
project-01-ecommerce/
├── src/
│   ├── extract.py       # load 9 CSVs into DataFrames
│   ├── transform.py     # merge tables, clean nulls, feature engineering
│   ├── load.py          # push to PostgreSQL via SQLAlchemy
│   └── analyze.py       # run queries, generate charts
├── sql/
│   ├── schema.sql       # table definitions
│   └── queries.sql      # 7 analytical queries
├── notebooks/
│   └── exploration.ipynb
└── output/charts/       # generated charts (gitignored)
```

## Setup

```bash
pip install -r requirements.txt
```

Create a PostgreSQL database named `olist`. Update `DB_URL` in `src/load.py` and `src/analyze.py` with your credentials.

Download the dataset from Kaggle and place all 9 CSV files inside `data/`.

## How to Run

```bash
# step 1 - transform and load data into postgres
python src/load.py

# step 2 - run queries and generate charts
python src/analyze.py
```

Charts are saved to `output/charts/`.

## Analytical Queries

| # | Query |
|---|---|
| 1 | Monthly revenue trend |
| 2 | Top 10 product categories by revenue |
| 3 | Average delivery time by state |
| 4 | Order volume by day of week |
| 5 | Top sellers by revenue |
| 6 | One-time vs repeat customer ratio |
| 7 | Revenue lost to late deliveries |

## Charts

- `monthly_revenue.png` — revenue trend over time
- `top_categories.png` — top 10 categories by revenue
- `delivery_by_state.png` — average delivery days per state
- `orders_by_dow.png` — order volume by day of week

## What I Learned

- Handling messy real-world data — nulls, wrong dtypes, multiple join keys across 9 tables
- SQLAlchemy for loading DataFrames into PostgreSQL
- Writing analytical SQL on a ~100k row dataset
- Building an end-to-end pipeline from raw CSVs to charts
