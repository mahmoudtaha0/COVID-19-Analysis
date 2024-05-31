import sqlite3
import csv
import pandas as pd

# Read data file
df = pd.read_csv('COVID-19 Dataset.csv')

# Convert Date from DD-MM-YYYY to YYYY-MM-DD
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')

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

# start_date and end_date
dates = """
SELECT MIN(Date) AS start_date, MAX(Date) AS end_date FROM covid_pandemic
"""
Dates = pd.read_sql_query(dates, conn)
print(Dates)

months = """
SELECT COUNT(DISTINCT strftime('%Y-%m', Date)) AS number_of_months FROM covid_pandemic
"""
number_of_months = pd.read_sql_query(months, conn)
print(number_of_months)

# Monthly average for confirmed, deaths, and recovered
monthly_averages_query = """
SELECT strftime('%Y-%m', Date) AS MonthYear,
AVG(Confirmed) AS average_confirmed,
AVG(Deaths) AS average_deaths,
AVG(Recovered) AS average_recovered
FROM covid_pandemic
GROUP BY MonthYear
ORDER BY MonthYear;
"""

monthly_averages = pd.read_sql_query(monthly_averages_query, conn)
print(monthly_averages)

# Close connection
# connection.close()