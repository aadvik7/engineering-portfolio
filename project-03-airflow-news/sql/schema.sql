-- articles table
-- url is unique to prevent duplicate inserts

CREATE TABLE IF NOT EXISTS articles (
    id SERIAL PRIMARY KEY,
    title TEXT,
    source VARCHAR(200),
    description TEXT,
    url TEXT UNIQUE,
    published_at TIMESTAMP,
    content TEXT,
    clean_title TEXT,
    clean_description TEXT,
    fetched_at TIMESTAMP DEFAULT NOW()
);
