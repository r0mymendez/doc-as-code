import sqlite3
import pandas as pd
import os

# Database name
db_name = "data/hospital.db"

# Connect to the database
connection = sqlite3.connect(db_name)

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Create the PATIENTS table
cursor.execute('''CREATE TABLE IF NOT EXISTS PATIENTS (
                    Id TEXT PRIMARY KEY,
                    BIRTHDATE DATE,
                    DEATHDATE DATE,
                    SSN TEXT,
                    DRIVERS TEXT,
                    PASSPORT TEXT,
                    PREFIX TEXT,
                    FIRST TEXT,
                    LAST TEXT,
                    SUFFIX TEXT,
                    MAIDEN TEXT,
                    MARITAL TEXT,
                    RACE TEXT,
                    ETHNICITY TEXT,
                    GENDER TEXT,
                    BIRTHPLACE TEXT,
                    ADDRESS TEXT,
                    CITY TEXT,
                    STATE TEXT,
                    COUNTY TEXT,
                    FIPS TEXT,
                    ZIP TEXT,
                    LAT REAL,
                    LON REAL,
                    HEALTHCARE_EXPENSES REAL,
                    HEALTHCARE_COVERAGE REAL,
                    INCOME INTEGER
                  )''')

# Create the VERSION_DATABASE table
cursor.execute('''CREATE TABLE IF NOT EXISTS VERSION_DATABASE (
                    version INTEGER,
                    date TIMESTAMP,
                    active INTEGER);''')

# Insert initial version data
try:
    cursor.execute('INSERT INTO VERSION_DATABASE (version, date, active) VALUES (?, ?, ?)', 
                   (1, pd.Timestamp.now().isoformat(), 1))
except sqlite3.IntegrityError:
    print("Version data already exists.")

# Commit changes
connection.commit()

# Check if the CSV file exists
csv_file_path = 'data/patients.csv'
if os.path.exists(csv_file_path):
    try:
        # Load the CSV file
        patients_df = pd.read_csv(csv_file_path)
        # Insert data into the PATIENTS table
        patients_df.to_sql('PATIENTS', connection, if_exists='replace', index=False)
        print("Patient data loaded successfully.")
    except Exception as e:
        print("Error loading data from CSV file:", e)
else:
    print("CSV file does not exist:", csv_file_path)

# Close the connection
connection.close()
