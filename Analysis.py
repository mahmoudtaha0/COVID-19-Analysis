import sqlite3
import csv
import pandas as pd

# Read data file
df = pd.read_csv('COVID-19 Dataset.csv')
# Create an SQLite database
conn = sqlite3.connect('covid.db')
# Load data file to SQLite
df.to_sql('covid-pandemic', conn, if_exists='replace')
# Close connection
# connection.close()