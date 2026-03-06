import pandas as pd
import sqlite3

def csv_to_sqlite(csv_filename, db_filename, table_name):
    # Load the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_filename)

    # Add the additional 'year' column with the value '2025'
    df['year'] = '2025'

    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_filename)

    # Write the DataFrame to the SQLite database table
    # if_exists='replace' ensures it overwrites the table if it already exists
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    # Define file names and table name
    input_csv = "field-day-2025.csv"
    output_db = "field_day_2025.db"
    db_table = "field_day"
    
    # Execute the import
    csv_to_sqlite(input_csv, output_db, db_table)
    print(f"Successfully imported {input_csv} into {output_db} under the table '{db_table}'.")
