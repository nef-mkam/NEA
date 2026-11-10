import sqlite3

conn = sqlite3.connect("gne_21.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS line (
    line_no TEXT PRIMARY KEY,
    route_name TEXT NOT NULL,
    direction TEXT
);

CREATE TABLE IF NOT EXISTS stops (
    stop_id INTEGER PRIMARY KEY,
    stop_name TEXT NOT NULL,
    latitude REAL,
    longitude REAL
);

CREATE TABLE IF NOT EXISTS stop_times (
    trip_id INTEGER NOT NULL,
    line_no TEXT NOT NULL,
    stop_id INTEGER NOT NULL,
    arrival_time TEXT NOT NULL,
    departure_time TEXT NOT NULL,
    stop_sequence INTEGER NOT NULL,
    PRIMARY KEY (trip_id, stop_sequence),
    FOREIGN KEY (line_no) REFERENCES routes(line_no),
    FOREIGN KEY (stop_id) REFERENCES stops(stop_id)
);
""").