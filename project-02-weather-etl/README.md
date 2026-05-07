# Weather ETL Pipeline

Automated pipeline that fetches live weather data for 5 Indian cities every hour using the OpenWeatherMap API, transforms the JSON response, and stores readings in PostgreSQL. Runs continuously with a scheduler and handles API failures gracefully.

## Stack

- Python 3.10
- Requests
- PostgreSQL + SQLAlchemy
- python-dotenv
- schedule

## Cities

Delhi, Mumbai, Bangalore, Chennai, Kolkata

## Project Structure

```
project-02-weather-etl/
├── src/
│   ├── extract.py      # hit openweathermap api per city
│   ├── transform.py    # parse JSON into clean dict
│   ├── load.py         # insert into postgres with dedup
│   └── pipeline.py     # wires E→T→L + scheduler
├── sql/
│   └── schema.sql      # weather_readings table
├── config.py           # city list, api url, interval
└── .env.example        # env variable template
```

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your credentials:

```
OWM_API_KEY=your_openweathermap_api_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=weather
DB_USER=postgres
DB_PASSWORD=your_password
```

Get a free API key at [openweathermap.org](https://openweathermap.org/api).

Create the database table:

```bash
psql -d weather -f sql/schema.sql
```

## How to Run

```bash
python src/pipeline.py
```

Pipeline runs immediately on start, then every 60 minutes. Logs each fetch with timestamp. Skips cities that fail API calls instead of crashing.

## What I Learned

- Working with REST APIs and parsing nested JSON
- Storing time-series data in PostgreSQL
- Writing dedup logic to avoid duplicate inserts on repeated runs
- Using the `schedule` library for lightweight task scheduling
- Proper error handling for network failures
