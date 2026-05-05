-- weather readings table

CREATE TABLE IF NOT EXISTS weather_readings (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    temp FLOAT,
    feels_like FLOAT,
    humidity INT,
    pressure INT,
    weather_desc VARCHAR(200),
    wind_speed FLOAT,
    wind_gust FLOAT,
    rain_1h FLOAT,
    fetched_at TIMESTAMP
);
