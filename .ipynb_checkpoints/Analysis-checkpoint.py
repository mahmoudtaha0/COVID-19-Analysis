import sqlite3
import csv
import pandas as pd

# Read data file
df = pd.read_csv('COVID-19 Dataset.csv')

# Create an SQLite database
conn = sqlite3.connect('covid.db')

# Load data file to SQLite
df.to_sql('covid_pandemic', conn, if_exists='replace')

query = """ SELECT * FROM covid_pandemic WHERE Province = 'Afghanistan'"""

results = pd.read_sql_query(query, conn)

print(results)
# Close connection
# connection.close()