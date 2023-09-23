import re
import pandas as pd

# Read the CSV file
try:
    df = pd.read_csv('Checking - 8011_09-22-2022_09-26-2023.csv')
except FileNotFoundError:
    print("CSV file not found.")
    exit()

# List of keywords to search for
keywords = ["PEACEHEALTH", "CITY OF EUGENE", "UO TRANS SVCS", "UO UNIVERSITY DIEUGENE"]

# Loop through each keyword
final_total_charge = 0

for keyword in keywords:
    # Use regex to filter the DataFrame
    pattern = re.compile(f".*{keyword}.*", re.IGNORECASE)
    filtered_df = df[df["Name"].str.match(pattern)]


    # Check if any records were found
    if filtered_df.empty:
        print(f"No records found for keyword: {keyword}")
    else:
        # Calculate and display the total sum
        total_sum = filtered_df["Amount"].sum()  # Make sure the column name matches your CSV
        print(f"\nTotal Sum for {keyword}: {total_sum}")
        final_total_charge += total_sum

        # Display the filtered DataFrame
        print(filtered_df)
        print (total_sum / 12)

print(final_total_charge)

percentcalc = input(f'If you reduce your charges in these areas by this percentage (no percent sign): ')

reduction = final_total_charge * (int(percentcalc) / 100)

print(f'You can save ${-1 * reduction} dollars next year, or ${( -1* reduction) / 12} per month. Big bucks, son!')