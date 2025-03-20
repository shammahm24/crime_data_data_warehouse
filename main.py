import sqlite3
import pandas as pd

df = pd.read_csv('./data/cleaned_crime_data.csv')

conn = sqlite3.connect("normalized_crime_data.db")
cursor = conn.cursor()

# insert unique locations
for _, row in df[['LOCATION', 'LAT', 'LON']].drop_duplicates().iterrows():
    cursor.execute("INSERT OR IGNORE INTO locations (location, latitude, longitude) VALUES (?, ?, ?)",
                   (row['LOCATION'], row['LAT'], row['LON']))
    
# insert unique victims
for _, row in df[['Vict Age', 'Vict Sex', 'Vict Descent']].drop_duplicates().iterrows:
    cursor.execute("INSERT OR IGNORE INTO victims (age, sex, descent) VALUES (?, ?, ?)",
                   (row['Vict Age'], row['Vict Sex'], row['Vict Descent']))
    
# insert unique crime codes
for _, row in df[['Crm Cd', 'Crm Cd Desc']].drop_duplicates().iterrows():
    cursor.execute("INSERT OR IGNORE INTO crime_codes (crime_code, description) VALUES (?, ?)",
                   (row['Crm Cd'], row['Crm Cd Desc']))

# insert unique weapons
for _, row in df[['Weapon Used Cd', 'Weapon Desc']].drop_duplicates().iterrows():
    cursor.execute("INSERT OR IGNORE INTO weapons (weapon_code, description) VALUES (?, ?)",
                   (row['Weapon Used Cd'], row['Weapon Desc']))
    
 # insert unique statuses
for _, row in df[['Status', 'Status Desc']].drop_duplicates().iterrows():
    cursor.execute("INSERT OR IGNORE INTO statuses (status, description) VALUES (?, ?)",
                   (row['Status'], row['Status Desc']))

conn.commit()   

# After tables are created
# insert Crime Reports
for _, row in df.iterrows():
    # Get foreign keys
    cursor.execute("SELECT location_id FROM locations WHERE location = ?", (row['LOCATION'],))
    location_id = cursor.fetchone()[0]

    cursor.execute("SELECT victim_id FROM victims WHERE age = ? AND sex = ? AND descent = ?",
                   (row['Vict Age'], row['Vict Sex'], row['Vict Descent']))
    victim_id = cursor.fetchone()[0]

    cursor.execute("SELECT crime_code FROM crime_codes WHERE crime_code = ?", (row['Crm Cd'],))
    crime_code = cursor.fetchone()[0]

    cursor.execute("SELECT weapon_id FROM weapons WHERE weapon_code = ?", (row['Weapon Used Cd'],))
    weapon_id = cursor.fetchone()[0] if cursor.fetchone() else None

    cursor.execute("SELECT status_id FROM statuses WHERE status = ?", (row['Status'],))
    status_id = cursor.fetchone()[0]

    # Insert into crime_reports
    cursor.execute("""
        INSERT INTO crime_reports (dr_no, date_reported, date_occurred, time_occurred, area, area_name, rpt_dist_no, part_1_2, crime_code, location_id, victim_id, weapon_id, status_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (row['DR_NO'], row['Date Rptd'], row['DATE OCC'], row['TIME OCC'], row['AREA'], row['AREA NAME'], row['Rpt Dist No'],
          row['Part 1-2'], crime_code, location_id, victim_id, weapon_id, status_id))

conn.commit()
conn.close()