# crime_data_data_warehouse
Python + Sqlite data warehouse for California crime data from 2020 to 2025 March.
Source : https://catalog.data.gov/dataset/crime-data-from-2020-to-present

# Buidling Data Warehouse with ETL
## Extraction
Extract data from California crime data set in csv format and clean data.

### Cleaning Data
1. Remove null values in key fields. (This data set only had missing data from a
 few rows under Status).
2. Drop non-essential columns with multiple rows of missing data.
3. Fill in missing values for remaining columns with most appropriate value.
    1. *Vict Age* - Integer age value can be filled in with the median since avarage
    will be more skewed do to the number of missing values.
    2. *Weapon Desc* - Use UNKNOWN value for weapons without description
    3. *Weapon Used Cd* - Code for unknow weapons is 0
    4. *Mocodes* - 0 for missing data
    5. *Vict Sex* - Replaced unknown sex with **X** matching existing data
    6. *Premis Cd* - 0 for unknown premise
    7. *Premis Desc* - Unknown for missing values
    8. *Vict Descent* - **X** for unknown values for race.
4. Remove duplicates based on *DR_NO* which is unique for each row

## Transformation
Create normalized data base to reduce redundancy and imporve efficiency

### Identify Entities and Relationships
1. *crime_reports* - information about each incident
2. *locations* - unique location data from the data set
3. *victims* -  victim information
4. *crime_codes* -  unique crime codes
5. *weapons* - unique weapons details
6. *statuses* - unique states codes

### ERD Diagram
![](https://github.com/shammahm24/crime_data_data_warehouse/blob/main/erd.png)

## Load
Load structured data into newly created database for further processing and reporting
by data and analytics teams.
Database of choice for this project is SQLite for the following reasons:
1. Lightweight and serverless so it can be run on a local system
2. Fast
3. Free and Open Source
4. Does not require additional configuraiton
5. Compatible with multiple platforms

# Project Expansion
## Full Scale Data Warehouse Design
![](https://github.com/shammahm24/crime_data_data_warehouse/blob/main/AWS%20Data%20Warehouse.drawio.png)

## Next Steps
1. Build Quiries and reports 
2. API for data access via Cloud or self hosted VPS
3. Visualization with Tableau
    1. Crime heat maps
    2. Crime trends
4. Automation using Apache Airflow and build **Data Pipelines**

# Setup
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
