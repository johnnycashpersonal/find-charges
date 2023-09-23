import re
import pandas as pd
import sqlite3

# Read the CSV file
try:
    df = pd.read_csv('Checking - 8011_09-22-2022_09-26-2023.csv')
except FileNotFoundError:
    print("CSV file not found.")
    exit()

# Create SQLite database and table
conn = sqlite3.connect("Financialdata.db")
df.to_sql("all_data", conn, if_exists= 'replace')

# List of keywords to search for
keywords = ["RECURRING"]

# Loop through each keyword
final_total_charge = 0

for keyword in keywords:
    # Use regex to filter the DataFrame
    pattern = re.compile(f".*{keyword}.*", re.IGNORECASE)
    filtered_df = df[df["Name"].str.match(pattern)]

    # Insert the filtered DataFrame into a new SQLite table
    filtered_df.to_sql("filtered_data", conn, if_exists='replace')


    # Check if any records were found
    if filtered_df.empty:
        print(f"No records found for keyword: {keyword}")
    else:
        # Query SQLite table to get all 'Recurring' line items
        query = "SELECT * FROM filtered_data"
        result_df = pd.read_sql_query(query, conn)
        print(result_df)

        # Calculate and display the total sum
        total_sum = filtered_df["Amount"].sum()  # Make sure the column name matches your CSV
        print(f"\nTotal Sum for {keyword}: {total_sum}")
        final_total_charge += total_sum

        print (total_sum / 12)

print(final_total_charge)