import sqlite3
import csv
import pandas as pd

# Read data file
df = pd.read_csv('COVID-19 Dataset.csv')

# Create an SQLite database
conn = sqlite3.connect('covid.db')

# Load data file to SQLite
df.to_sql('covid_pandemic', conn, if_exists='replace')

# Display rows containing null values
nullValues = """
SELECT * FROM covid_pandemic 
WHERE "Country/Region" IS NULL 
OR Province IS NULL 
OR Latitude IS NULL 
OR Longitude IS NULL 
OR Date IS NULL 
OR Confirmed IS NULL 
OR Deaths IS NULL 
OR Recovered IS NULL
"""
results = pd.read_sql_query(nullValues, conn)
print(results)

# Replace null values' rows with 0
replaceNull = """
UPDATE covid_pandemic
SET "Country/Region" = '0',
    Province = '0',
    Latitude = 0,
    Longitude = 0,
    Date = '0',
    Confirmed = 0,
    Deaths = 0,
    Recovered = 0
WHERE "Country/Region" IS NULL
   OR Province IS NULL
   OR Latitude IS NULL
   OR Longitude IS NULL
   OR Date IS NULL
   OR Confirmed IS NULL
   OR Deaths IS NULL
   OR Recovered IS NULL
"""
conn.execute(replaceNull)
conn.commit()

# Check total number of rows
totalRows = """
SELECT COUNT(*) FROM covid_pandemic
"""
count = pd.read_sql_query(totalRows, conn)
print(count)

results = pd.read_sql_query(nullValues, conn)
print(results)



# Close connection
# connection.close()