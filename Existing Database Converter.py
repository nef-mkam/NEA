import sqlite3
import pandas as pd

timetable = pd.read_csv("21 TimeTable - Newcastle Weekdays.csv")

timetable.columns = timetable.columns.str.strip()

SQL_link = sqlite3.connect("timetable.db")

timetable.to_sql("", SQL_link, if_exists="replace")

SQL_link.close()
