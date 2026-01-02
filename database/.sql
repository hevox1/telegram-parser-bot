CREATE DATABASE bot_db;

CREATE TABLE sources (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    is_activate BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);