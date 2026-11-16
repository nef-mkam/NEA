import sqlite3
import csv

conn = sqlite3.connect("gne_21.db")
cursor = conn.cursor()

cursor.execute("""
    INSERT OR IGNORE INTO line (line_no, route_name, direction)
    VALUES (?, ?, ?)
    """, ("21", "Newcastle - Durham", "Durham"))

with open("21 TimeTable - Newcastle Weekdays.csv", newline="") as gne_21:
    gne_21_list = list(csv.reader(gne_21))

rows_to_insert = []

for y in range(1,115):

    stop_sequence = 1

    for i in range (1,80):
        try:
            stop_name = gne_21_list[83 + i][1]
            arrival_time = gne_21_list[83 + i][1 + y].strip()
            departure_time = gne_21_list[83 + i][2 + y].strip()
            if (not arrival_time or arrival_time == "-") and (not departure_time or departure_time == "-"):
                continue

            rows_to_insert.append(("21", stop_name, arrival_time, departure_time, stop_sequence))
            stop_sequence += 1
        except IndexError:
            continue

cursor.executemany("""
    INSERT OR REPLACE INTO stop_times (line_no, stop_name, arrival_time, departure_time,stop_sequence)
    VALUES (?, ?, ?, ?, ?, ?)
""", rows_to_insert)

conn.commit()
conn.close()
print("Imported CSV into Database")

