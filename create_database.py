import sqlite3

conn = sqlite3.connect("normalized_crime_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS locations (
               location_id INTEGER PRIMARY KEY AUTOINCREMENT,
               location TEXT UNIQUE,
               latitude REAL,
               longitude REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS victims (
               victim_id INTEGER PRIMARY KEY AUTOINCREMENT,
               age INTEGER,
               sex TEXT,
               descent TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS crime_codes (
               crime_code INTEGER PRIMARY KEY,
               description TEXT UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS weapons (
               weapon_id INTEGER PRIMARY KEY AUTOINCREMENT,
               weapon_code INTEGER UNIQUE,
               description TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS statuses (
               status_id INTEGER PRIMARY KEY AUTOINCREMENT,
               status TEXT UNIQUE,
               description TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS crime_reports (
               dr_no INTEGER PRIMARY KEY,
               date_reported TEXT,
               date_occured TEXT,
               time_occured INTEGER,
               area INTEGER,
               area_name TEXT,
               rpt_dist_no INTEGER,
               part_1_2 INTERGER,
               crime_code INTEGER,
               location_id INTEGER,
               victim_id INTEGER,
               weapon_id INTEGER,
               status_id INTEGER,
               FOREIGN KEY (crime_code) REFERENCES crime_codes(crime_code),
               FOREIGN KEY (location_id) REFERENCES locations(location_id),
               FOREIGN KEY (victim_id) REFERENCES victims(victim_id),
               FOREIGN KEY (weapon_id) REFERENCES victims(weapon_id),
               FOREIGN KEY (status_id) REFERENCES statuses(status_id)
);
""")

conn.commit()
conn.close()