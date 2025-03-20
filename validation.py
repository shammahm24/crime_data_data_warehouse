import sqlite3

conn = sqlite3.connect("normalized_crime_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM crime_reports LIMIT 5")
print(cursor.fetchall())

conn.close()